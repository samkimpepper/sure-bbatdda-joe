from django.shortcuts import render

def chat(request):
    return render(request, 'chat_index.html')
    # return render(request, 'chat.html')

def room(request, room_name, goods_id, seller_id, buyer_id):
    return render(request, 'chat_room.html', {
        'room_name': room_name,
        'goods_id': goods_id,
        'seller_id': seller_id,
        'buyer_id': buyer_id,
    })