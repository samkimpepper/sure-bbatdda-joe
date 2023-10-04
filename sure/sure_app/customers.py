import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, Chat, User
from django.core.serializers.json import DjangoJSONEncoder
from channels.layers import get_channel_layer
from django.core.cache import cache

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        self.room_name = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        
        # 캐시에 저장
        user_id = User.objects.get(id=self.scope["user"].id).id
        self.add_user_to_cache(str(user_id), self.room_name)

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        
        # 캐시에서 삭제
        user_id = User.objects.get(id=self.scope["user"].id).id
        self.remove_user_from_cache(self.room_name, str(user_id))


    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        message = text_data_json["message"] # 메시지 내용 추출
        sender = text_data_json["sender"]  # 보내는 사람 추출
        
        chat = Chat.objects.get(id=chat_id)
        sender = User.objects.get(id=sender)
        
        if chat.user1 == sender: receiver_id = chat.user2.id
        else: receiver_id = chat.user1.id
        connected_users = self.get_connected_users(self.room_name)
        
        if str(receiver_id) in connected_users:
            message_obj = Message.objects.create(chat=chat, text=message, sender=sender, status=True) 
        else:
            message_obj = Message.objects.create(chat=chat, text=message, sender=sender, status=False)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat_message",
                "message": message,
                "send_date": str(message_obj.send_date),
                "sender": sender.id,  # username을 함께 전송
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        send_date = event["send_date"]
        sender = event["sender"]  # username을 추출

        # Send message and username to WebSocket
        await self.send(text_data=json.dumps({
            "message": message,
            "send_date": send_date,
            "sender": sender  # username도 함께 전송
        }))
        
    def add_user_to_cache(self, user_id, room_id):
        # 연결된 사용자를 캐시에 저장
        connected_users_key = f'connected_users_{room_id}'
        connected_users = cache.get(connected_users_key, set())
        connected_users.add(str(user_id))  # 사용자 ID를 문자열로 변환
        cache.set(connected_users_key, connected_users)

        print(f'Added user {user_id} to connected users for room {room_id}')
        print(f'Connected users for room {room_id} after adding: {list(connected_users)}')
    
    def remove_user_from_cache(self, room_id, user_id):
        connected_users_key = f'connected_users_{room_id}'
        connected_users = cache.get(connected_users_key, set())
        connected_users.discard(user_id)
        print(f'Remove users for room {room_id} after fetching: {connected_users}')
        cache.set(f'connected_users_{room_id}', connected_users)


    def get_connected_users(self, room_id):
        # 캐시에서 연결된 사용자를 가져옴
        connected_users_key = f'connected_users_{room_id}'
        connected_users = cache.get(connected_users_key, set())
        print(f'Connected users for room {room_id} before fetching: {connected_users}')
        return (connected_users)