from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from channels.generic import BaseConsumer
from channels.generic.websockets import WebsocketConsumer
from channels.generic.websockets import JsonWebsocketConsumer

from .models import *


class CustomerConsumer(WebsocketConsumer):

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
        print('customer added, mess:', message)
        requested_groups = self.build_requested_groups_for_user(message)
        print("grp:", requested_groups)
        print("grp:", type(requested_groups))
        reply = []
        for group in requested_groups:
            if not self.group_exist(group):
                reply.append({group: False})
                continue
            reply.append({group: True})
            self.add_user_to_group(message, group)

        self.message.reply_channel.send({'accept': True})

    def build_requested_groups_for_user(self, message):
        groups = str(message.content['query_string']).split("=")[1][:-1].split(',')
        for index in range(len(groups)):
            grp = groups[index]
            grp = grp.replace('%20', '')
            groups[index] = grp
        return groups

    def group_exist(self, group_name):
        return Line.objects.filter(name=group_name).exists()

    def add_user_to_group(self, message, group_name):
        Group(group_name).add(message.reply_channel)

    def get_all_groups_names(self):
        return Line.objects.all().values_list('name', flat=True)

    def receive(self, text=None, bytes=None, **kwargs):
        """
        Called when a message is received with either text or bytes
        filled out.
        """
        # Simple echo
        # print('msg:', dict(text))
        print('msg:', type(text))
        self.send(text=text, bytes=bytes)

    def disconnect(self, message, **kwargs):
        print("on close::::")
        for group_name in self.get_all_groups_names():
            Group(group_name).discard(message.reply_channel)


class BusConsumer(WebsocketConsumer):

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
        Group(my_line.name).send({"new_bus": my_bus_info})

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

    def receive(self, text=None, bytes=None, **kwargs):
        """
        Called when a message is received with either text or bytes
        filled out.
        """
        # Simple echo
        self.send(text=text, bytes=bytes)

    def disconnect(self, message, **kwargs):
        """
        Perform things on connection close
        """
        pass