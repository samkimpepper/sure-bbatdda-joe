from django.urls import re_path
from . import customers
from .alarm_consumers import AlarmConsumer

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_id>\d+)/$", customers.ChatConsumer.as_asgi()),
    re_path(r"ws/alarm/", AlarmConsumer.as_asgi()),
]
