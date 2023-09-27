from django.shortcuts import render
from ..models import Chat

def chatting(request, chat_id):
    # TODO: 고정값 동적으로 변경
    
    goods_id = 1
    seller_id = 2
    buyer_id = 3
    
    print(goods_id, seller_id, buyer_id)
    
    new_chat = Chat.objects.get_or_create(
        goods_id=goods_id,
        seller_id=seller_id,
        buyer_id=buyer_id
    )
    
    context = {"chat_id": new_chat[0].id, 
               "goods_id": goods_id, 
               "seller_id": seller_id, 
               "buyer_id": buyer_id
            }
    
    return render(request, 'chat.html', context) 