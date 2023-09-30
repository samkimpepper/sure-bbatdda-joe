from django.shortcuts import render
from django.http import JsonResponse
from ..models import Chat, User, Message


def chatting(request, chat_id):
    # TODO: goods_id, user2 고정값 동적으로 변경
    goods_id = 1 # 채팅으로 넘어온 매물
    user1 = request.user # 채팅을 시작한 사람 (구매자)
    user2 = User.objects.get(id=21) # 채팅을 받는 사람 (판매자)
    
    # user가 참여한 모든 채팅방 목록 가져오기
    chat_list = []
    chat_list += list(Chat.objects.filter(user1 = user1).select_related("user1"))
    chat_list += list(Chat.objects.filter(user2 = user1).select_related("user2"))
    chat_list.sort(key=lambda x: x.id)
    
    
    # 채팅방의 마지막 메시지 가져오기
    message_list = []
    for chat in chat_list:
        message_queryset = Message.objects.filter(chat_id=chat.id)
        if message_queryset.exists(): message_list.append(list(message_queryset)[-1])
        else: message_list.append(None)
        

    new_chat = Chat.objects.get_or_create(
        goods_id=goods_id,
        user1=user1,
        user2=user2
    )
    
    context = {
        "user_id": request.user.id,
        "chat_id": new_chat[0].id, 
        "goods_id": goods_id, 
        "user_id": user1.id,
        "chat_and_mesage_list" : zip(chat_list, message_list)
    }
    
    return render(request, 'chat.html', context) 

# 메시지 기록을 불러오는 함수입니다.
def messages(request, chat_id):
    messages = list(Message.objects.filter(chat_id=chat_id).values())
    return JsonResponse(messages, safe=False)