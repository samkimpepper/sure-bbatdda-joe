import json
from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import parse_qs
from channels.db import database_sync_to_async

from .models import User, Alarm
from .serializers import AlarmSerializer

class AlarmConsumer(AsyncWebsocketConsumer):

    @database_sync_to_async
    def get_user_by_id(self, user_id):
        return User.objects.get(id=user_id)
    
    @database_sync_to_async
    def get_unread_alarms(self, user_id):
        return Alarm.objects.filter(user=user_id, is_read=False)
    
    @database_sync_to_async
    def get_unread_alarm_cnt(self, user_id):
        return Alarm.objects.filter(user=user_id, is_read=False).count()
    
    async def connect(self):
        user_id = parse_qs(self.scope["query_string"].decode("utf8"))["user_id"][0]

        self.user = await self.get_user_by_id(user_id)
        self.group_name = f"user{self.user.id}"
        print("group_name: " + self.group_name)

        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

        alarms = await self.get_unread_alarms(user_id)
        serializer = AlarmSerializer(alarms, many=True)

        await self.channel_layer.group_send(
            self.group_name, {
                "type": "unread_alarms",
                "alarm_cnt": await self.get_unread_alarm_cnt(user_id),
                "alarms": serializer.data
            }
        )
                                            
    async def receive_review(self, event):
        print("receive!!")
        content = event["content"]
        link = event["link"]
        alarm_id = event["alarm_id"]

        await self.send(text_data=json.dumps({
            "content": content,
            "link": link,
            "alarm_id": alarm_id
        }))

    async def unread_alarms(self, event):
        print("alarm cnt!!!")
        alarm_cnt = event["alarm_cnt"]
        alarms = event["alarms"]

        await self.send(text_data=json.dumps({
            "type": "unread_alarms",
            "alarm_cnt": alarm_cnt,
            "alarms": alarms
        }))

    async def alarm_cnt(self, event):

        await self.send(text_data=json.dumps(event))


