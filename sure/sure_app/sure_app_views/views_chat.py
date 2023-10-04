from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import Chat, User, Message, Goods

# 참여한 모든 채팅방 목록을 가져오는 함수
def _get_chat_list(me):
    chat_list = set()
    chat_list.update(set(Chat.objects.filter(user1_id = me.id).select_related("user1")))
    chat_list.update(set(Chat.objects.filter(user2_id = me.id).select_related("user2")))
    chat_list = list(chat_list)
    chat_list.sort(key=lambda x: x.id)
    return chat_list

# 각 채팅방의 마지막 메시지를 가져오는 함수
def _get_last_message_list(chat_list):
    last_message_list = []
    for chat in chat_list:
        message_queryset = Message.objects.filter(chat_id=chat.id).order_by('send_date')
        if message_queryset.exists(): last_message_list.append(list(message_queryset)[-1])
        else: last_message_list.append(None)
    return last_message_list

def chatting(request, goods_id=None, you_id=None):
    me = request.user # 채팅을 시작한 사람 (구매자)
    print(me)
    chat_list= _get_chat_list(me)
    print(chat_list)
    last_message_list = _get_last_message_list(chat_list)
    print(last_message_list)
    
    # 매물 목록에서 넘어왔다면 
    if goods_id and you_id:
        goods = get_object_or_404(Goods, id=goods_id)
        you = get_object_or_404(User, id=you_id)
        # 채팅방 생성/가져오기
        new_chat = Chat.objects.get_or_create(
            goods=goods,
            user1=me,
            user2=you
        )
        
        context = {
            "chat_id": new_chat[0].id, 
            "goods_id": goods_id, 
            "me": me,
            "you": you,
            "chat_and_message_list" : zip(chat_list, last_message_list)
        }
    
    # nav 바에서 넘어왔다면
    else:
        context = {
            "me": me,
            "chat_and_message_list" : zip(chat_list, last_message_list)
        }
    
    print(context)
    return render(request, 'chat.html', context) 

# 메시지 기록을 불러오는 함수입니다.
def messages(request, chat_id):
    messages = Message.objects.filter(chat_id=chat_id).order_by('send_date').values()
    
    # 메시지를 불러오면서 읽음 처리
    for message in list(messages):
        tmp = Message.objects.get(id=message['id'])
        tmp.status = True
        tmp.save()

    return JsonResponse(list(messages), safe=False)