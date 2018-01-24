import json
from time import sleep

from channels.handler import AsgiHandler
from channels import Group
from channels.generic import BaseConsumer
from channels.generic.websockets import WebsocketConsumer
from channels.generic.websockets import JsonWebsocketConsumer


from .models import *


class TTT(JsonWebsocketConsumer):
    # Set to True if you want it, else leave it out
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["test"]

    def connect(self, message, **kwargs):
        print('msg:', message.content)
        self.message.reply_channel.send({'accept': True})
        self.message.reply_channel.send({"bale": 22})
        print('yeaa')

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON content
        """
        # Simple echo
        print('content:', content)
        print('content:', type(content))
        self.send(content)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass


class CustomerConsumer(JsonWebsocketConsumer):

    # Set to True to automatically port users from HTTP cookies
    # (you don't need channel_session_user, this implies it)
    http_user = True

    # Set to True if you want it, else leave it out
    strict_ordering = False

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["test"]

    def build_requested_groups_for_user(self, message):
        if not message.content['query_string']:
            return []
        groups = str(message.content['query_string']).split("=")[1][:-1].split(',')
        for index in range(len(groups)):
            grp = groups[index]
            grp = grp.replace('%20', '')
            groups[index] = grp
        return groups

    def group_exist(self, group_name):
        return Line.objects.filter(name=group_name).exists()

    def add_user_to_group(self, group_name):
        Group(group_name).add(self.message.reply_channel)

    def discard_user_from_group(self, group_name):
        Group(group_name).discard(self.message.reply_channel)

    def get_all_groups_names(self):
        return Line.objects.all().values_list('name', flat=True)

    def build_groups_info_for_user(self, groups):
        groups_info = []
        for group in groups:
            group_info = self.build_group_info(group)
            groups_info.append(group_info)
        return {'groups': groups_info}

    def build_group_info(self, group_name: str):
        line = Line.objects.filter(name=group_name).prefetch_related('stations').prefetch_related('buses')
        if not line.exists():
            return {}
        line = line.first()
        print('line stations:', line.stations)
        print('line buses:', line.buses)
        group_info = {'line': dict(id=line.id, name=line.name),
                      'stations': self.build_group_stations_info(line.stations.all()),
                      'buses': self.build_group_buses_info(line.buses.all())}

        return group_info

    def build_group_stations_info(self, stations):
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
                'next_station': station.my_next_station_id,
                'prev_station': station.my_prev_station_id,
                'is_final_state': station.is_final_station,
                'bus_wait_time': station.bus_wait_time,
                'x_pos': station.x_pos,
                'y_pos': station.y_pos,
            })
        return stations_info

    def build_group_buses_info(self, buses):
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
                    discarded_groups.append(group)
                print('group:', group, 'discarded:D')
        added_groups_info = self.build_groups_info_for_user(added_groups)
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

    def connection_groups(self, **kwargs):
        """
        Called to return the list of groups to automatically add/remove
        this connection to/from.
        """
        return ["test"]

    def connect(self, message, **kwargs):
        print('bus added, mess:', message.content["query_string"])
        token = self.get_token_from_message(message)
        my_bus = Bus.objects.filter(token=token).select_related('line')
        if not my_bus.exists():
            print('no bus with token')
            self.message.reply_channel.send({"accept": False})
            return
        if my_bus.count() > 1:
            raise("more than 1 bus with token: " + str(token))
        self.message.reply_channel.send({"accept": True})
        print('bus with token')
        my_bus = my_bus.first()
        my_line = my_bus.line
        print('line:', my_line.name)
        Group(my_line.name).add(message.reply_channel)
        my_bus_info = self.get_bus_info(my_bus)
        self.group_send(my_line.name, {"new_bus": my_bus_info})

    def get_token_from_message(self, message):
        token = str(message.content["query_string"]).split("=")[1][:-1]
        print('token:', token)
        return token

    def get_bus_info(self, bus):
        bus_info = {'id': bus.id,
                    'line': bus.line,
                    'speed': bus.speed,
                    'x_pos': bus.x_pos,
                    'y_pos': bus.y_pos,
                    'prev_station': bus.prev_station.name,
                    'next_station': bus.next_station,
                    'is_on_station': bus.is_on_station,
                    'last_update_time': bus.last_update_time,
                    'token': bus.token}
        return bus_info

    def receive(self, content, **kwargs):
        """
        Called when a message is received with decoded JSON content
        """
        # Simple echo
        print('content:', content)
        print('content:', type(content))
        self.send(content)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass