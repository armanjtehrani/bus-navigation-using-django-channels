from channels.routing import route

from .consumers import *


channel_routing = [
    TTT.as_route(path=r"/cc/"),
    CustomerConsumer.as_route(path=r"^/customers/"),
    BusConsumer.as_route(path=r"^/buses/"),
]