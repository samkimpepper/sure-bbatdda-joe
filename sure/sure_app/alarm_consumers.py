import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from channels.db import database_sync_to_async

from .models import User

class AlarmConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def get_user_by_id(self, user_id):
        return User.objects.get(id=user_id)
    
    async def connect(self):
        user_id = parse_qs(self.scope["query_string"].decode("utf8"))["user_id"][0]

        self.user = await self.get_user_by_id(user_id)
        self.group_name = f"user{self.user.id}"
        print("group_name: " + self.group_name)

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive_review(self, event):
        print("receive!!")
        content = event["content"]
        link = event["link"]

        await self.send(text_data=json.dumps({
            "content": content,
            "link": link
        }))

    


