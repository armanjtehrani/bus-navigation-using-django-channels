from channels import Group
from channels.generic.websockets import JsonWebsocketConsumer

from .models import *


class GroupInfoManager:
    @staticmethod
    def build_groups_info_for_user(groups):
        groups_info = []
        for group in groups:
            group_info = GroupInfoManager.build_group_info(group)
            groups_info.append(group_info)
        return {'groups': groups_info}

    @staticmethod
    def build_group_info(group_name: str):
        line = Line.objects.filter(name=group_name).prefetch_related('stations').prefetch_related('buses')
        if not line.exists():
            return {}
        line = line.first()
        print('line stations:', line.stations.all())
        print('line buses:', line.buses.all())
        group_info = {'line': dict(id=line.id, name=line.name),
                      'stations': GroupInfoManager.build_group_stations_info(line.stations.all()),
                      'buses': GroupInfoManager.build_group_buses_info(line.buses.all())}

        return group_info

    @staticmethod
    def build_group_stations_info(stations):
        print('statins:', stations)
        if not stations.exists():
            print('nooo')
            return []
        print('yesss')
        stations_info = []
        for station in stations:
            stations_info.append({
                'id': station.id,
                'name': station.name,
                'line': station.line_id,
                'next_station': station.next_station_id,
                'prev_station': station.prev_station_id,
                'is_final_state': station.is_final_station,
                'bus_wait_time': station.bus_wait_time,
                'x_pos': station.x_pos,
                'y_pos': station.y_pos,
            })
        return stations_info

    @staticmethod
    def build_group_buses_info(buses):
        if not buses.exists():
            return []

        buses_info = []
        for bus in buses:
            buses_info.append({
                'id': bus.id,
                'line': bus.line_id,
                'speed': bus.speed,
                'x_pos': bus.x_pos,
                'y_pos': bus.y_pos,
                'prev_station': bus.prev_station_id,
                'next_station': bus.next_station_id,
                'is_on_station': bus.is_on_station,
                # 'last_update_time': bus.last_update_time,
            })
        return buses_info


class CustomerConsumer(JsonWebsocketConsumer):

    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    http_user = True

    # Set to True if you want it, else leave it out
    strict_ordering = False

    def group_exist(self, group_name):
        return Line.objects.filter(name=group_name).exists()

    def add_user_to_group(self, group_name):
        Group(group_name).add(self.message.reply_channel)

    def discard_user_from_group(self, group_name):
        Group(group_name).discard(self.message.reply_channel)

    def get_all_groups_names(self):
        return Line.objects.all().values_list('name', flat=True)

    def receive(self, content, **kwargs):
        added_groups = []
        discarded_groups = []

        new_groups = content.get('add', [])
        if isinstance(new_groups, list):
            for group in new_groups:
                if self.group_exist(group):
                    self.add_user_to_group(group)
                    added_groups.append(group)
                    print('group:', group, 'added:D')

        old_groups = content.get('discard', [])
        if isinstance(old_groups, list):
            for group in old_groups:
                if self.group_exist(group):
                    self.discard_user_from_group(group)
                    discarded_groups.append({'id': Line.objects.get(name=group).id, 'name': group})
                print('group:', group, 'discarded:D')
        added_groups_info = GroupInfoManager.build_groups_info_for_user(added_groups)
        print('msg:', type(added_groups_info))
        print('msg:', added_groups_info)
        all_groups_info = {'add': added_groups_info,
                           'discard': discarded_groups}
        print('data:', all_groups_info)
        self.send(all_groups_info)

    def disconnect(self, message, **kwargs):
        print("on close::::")
        for group_name in self.get_all_groups_names():
            Group(group_name).discard(message.reply_channel)


class BusConsumer(JsonWebsocketConsumer):

    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    http_user = True

    # Set to True if you want it, else leave it out
    strict_ordering = False

    def get_line_info_for_bus(self, line):
        line_info = {'id': line.id,
                     'name': line.name}
        return line_info

    def get_station_info_for_bus(self, station):
        station_info = {'id': station.id,
                        'name': station.name,
                        'x_pos': station.x_pos,
                        'y_pos': station.y_pos,
                        'bus_wait_time': station.bus_wait_time,
                        'is_final_station': station.is_final_station,
                        }
        return station_info

    def get_bus_info_for_bus(self, bus):
        bus_info = {'id': bus.id,
                    'line': bus.line.id,
                    'speed': bus.speed,
                    'x_pos': bus.x_pos,
                    'y_pos': bus.y_pos,
                    'prev_station': bus.prev_station.id,
                    'next_station': bus.next_station.id,
                    'is_on_station': bus.is_on_station,
                    # 'last_update_time': bus.last_update_time,
                    # 'token': bus.token
                    }
        return bus_info

    def get_token_from_content(self, content):
        return content.get('token', "")

    def get_bus_from_token(self, token):
        bus = Bus.objects.filter(token=token).select_related('line', 'prev_station', 'next_station')
        print('prev_station', bus.first().prev_station)
        print('next_station', bus.first().next_station)
        return bus

    def bus_status_is_unknown(self, content):
        bus_status = content.get('status')
        if bus_status == "unknown":
            return True
        return False

    def notify_bus_its_info(self, bus):
        bus_info = self.build_bus_info_for_itself(bus)
        self.send(bus_info)

    def build_bus_info_for_itself(self, bus):
        line_info = self.get_line_info_for_bus(bus.line)
        prev_station_info = self.get_station_info_for_bus(bus.prev_station)
        next_station_info = self.get_station_info_for_bus(bus.next_station)
        bus_info = self.get_bus_info_for_bus(bus)
        main_info = {'line': line_info,
                     'prev_station': prev_station_info,
                     'next_station': next_station_info,
                     'bus': bus_info}
        return main_info

    def bus_status_is_telling_new_position(self, content):
        bus_status = content.get('status')
        if bus_status == "new_pos":
            return True
        return False

    def bus_status_arrived_to_new_station(self, content):
        bus_status = content.get('status')
        if bus_status == "arrived_to_station":
            return True
        return False

    def update_bus_new_position(self, content, my_bus):
        bus_new_x_pos = content.get('x_pos')
        bus_new_y_pos = content.get('y_pos')
        if bus_new_x_pos is None or bus_new_y_pos is None:
            print('non')
            return False
        try:
            bus_new_x_pos = float(bus_new_x_pos)
            bus_new_y_pos = float(bus_new_y_pos)
        except:
            print('no float')
            return False
        my_bus.is_on_station = False
        my_bus.x_pos = bus_new_x_pos
        my_bus.y_pos = bus_new_y_pos
        my_bus.save()
        print('x:', my_bus.x_pos)
        print('y:', my_bus.y_pos)
        return True

    def update_bus_new_station(self, my_bus):
        print('new prev', my_bus.next_station)
        new_bus_prev_station = my_bus.next_station
        new_bus_next_station = self.calculate_bus_next_station(my_bus)
        print('new next:', new_bus_next_station)
        my_bus.prev_station = new_bus_prev_station
        my_bus.next_station = new_bus_next_station
        my_bus.is_on_station = True
        my_bus.x_pos = new_bus_prev_station.x_pos
        my_bus.y_pos = new_bus_prev_station.y_pos
        # my_bus.last_update_time = datetime.now
        my_bus.save()

    def calculate_bus_next_station(self, my_bus):
        print('prev next:')
        print('is:', my_bus.prev_station.next_station)
        if my_bus.prev_station.is_final_station:
            if my_bus.next_station.next_station_id == my_bus.prev_station_id:
                return my_bus.next_station.prev_station
            return my_bus.next_station.next_station
        if my_bus.next_station_id == my_bus.prev_station.next_station_id:
            return my_bus.next_station.next_station
        else:
            return my_bus.next_station.prev_station

    def notify_group_about_new_state(self, line):
        added_groups_info = GroupInfoManager.build_groups_info_for_user([line.name])
        all_groups_info = {'add': added_groups_info,
                           'discard': []}
        print('group info:', all_groups_info)
        self.group_send(line.name, all_groups_info)

    def receive(self, content, **kwargs):
        token = self.get_token_from_content(content)
        my_bus = self.get_bus_from_token(token)
        if not my_bus.exists():
            print('no bus with token')
            self.send({'status': 0, 'msg': 'token not acceptable'})
            return
        print('bus with token')
        my_bus = my_bus.first()
        # req = {'status': ['what is my state', 'new pos', {'x_pos': int, 'y_pos': int}, 'arrived to station']}

        if self.bus_status_is_unknown(content):
            print('unknown')
            self.notify_bus_its_info(my_bus)
        elif self.bus_status_is_telling_new_position(content):
            print('new pos')
            success_state = self.update_bus_new_position(content, my_bus)
            if not success_state:
                return
            self.notify_group_about_new_state(my_bus.line)
        elif self.bus_status_arrived_to_new_station(content):
            print('new station')
            self.update_bus_new_station(my_bus)
            print('bus new station updated')
            self.notify_bus_its_info(my_bus)
            print('bus itself notified')
            self.notify_group_about_new_state(my_bus.line)
            print('notif sent to group')
        # self.group_send(my_line.name, {"new_bus": my_bus_info})
