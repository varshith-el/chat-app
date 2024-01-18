from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from django.core.asgi import get_asgi_application
from chat import consumers

application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Add this line
    'websocket': URLRouter([
        re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
    ]),
})
