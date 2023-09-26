from django.urls import re_path

from . import customers

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<goods_id>\d+)/(?P<seller_id>\d+)/(?P<buyer_id>\w+)/$", customers.ChatConsumer.as_asgi()),
]
