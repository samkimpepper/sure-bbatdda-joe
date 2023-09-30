import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Chat, User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        # self.room_name = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_name = 32
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        message = text_data_json["message"] # 메시지 내용 추출
        sender = text_data_json["sender"]  # 보내는 사람 추출
        

        print(chat_id, message, sender)
        chat = Chat.objects.get(id=chat_id)
        sender = User.objects.get(id=sender)
        Message.objects.create(chat=chat, text=message, sender=sender) # 메시지 저장

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "sender": sender.id,  # username을 함께 전송
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender = event["sender"]  # username을 추출

        # Send message and username to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "sender": sender  # username도 함께 전송
        }))