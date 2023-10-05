from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from ..models import Chat, User, Message, Goods
import openai
import os
import json
from pathlib import Path

# Openai API key
BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRETS_DIR = BASE_DIR / '.secrets'
key = json.load(open(os.path.join(SECRETS_DIR, 'key.json')))
OPENAI_KEY = key['OPENAI_KEY']

# 참여한 모든 채팅방 목록을 가져오는 함수
def _get_chat_list(me):
    chat_list = set()
    chat_list.update(set(Chat.objects.filter(user1_id = me.id).select_related("user1")))
    chat_list.update(set(Chat.objects.filter(user2_id = me.id).select_related("user2")))
    chat_list = list(chat_list)
    chat_list.sort(key=lambda x: -x.id)
    return chat_list

# 각 채팅방의 마지막 메시지를 가져오는 함수
def _get_last_message_list(chat_list):
    last_message_list = []
    for chat in chat_list:
        message_queryset = Message.objects.filter(chat_id=chat.id).order_by('send_date')
        if message_queryset.exists(): last_message_list.append(list(message_queryset)[-1])
        else: last_message_list.append(None)
    return last_message_list

# 각 채팅방의 매물 이미지를 가져오는 함수
def _get_goods_image_list(chat_list):
    goods_image_list = []
    for chat in chat_list:
        goods_image_list.append(Goods.objects.get(id=chat.goods_id).img.url)
    return goods_image_list

def chatting(request, goods_id=None, you_id=None):
    me = request.user # 채팅을 시작한 사람 (구매자)
    chat_list= _get_chat_list(me)
    goods_img_list = _get_goods_image_list(chat_list)
    last_message_list = _get_last_message_list(chat_list)
    
    # 매물 목록에서 넘어왔다면 
    if goods_id and you_id:
        goods = get_object_or_404(Goods, id=goods_id)
        you = get_object_or_404(User, id=you_id)
        # 채팅방 생성/가져오기
        new_chat = Chat.objects.get_or_create(
            goods=goods,
            user1=me,
            user2=you
        )[0]
        
        print(new_chat)
        context = {
            "chat": new_chat, 
            "goods": goods, 
            "me": me,
            "you": you,
            "chat_and_message_list" : zip(chat_list, last_message_list, goods_img_list)
        }
    
    # nav 바에서 넘어왔다면
    else:
        context = {
            "me": me,
            "chat_and_message_list" : zip(chat_list, last_message_list, goods_img_list)
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

def bot(request):
    openai.api_key = OPENAI_KEY
    
    # 제목 필드값 가져옴
    prompt = request.POST.get("title")
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        # 반환된 응답에서 텍스트 추출해 변수에 저장
        message = response["choices"][0]["message"]["content"]
    except Exception as e:
        message = str(e)
    
    return JsonResponse({"message": message})