from django.urls import re_path

from . import customers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<chat_id>\d+)/$", customers.ChatConsumer.as_asgi()),
]
