from django.shortcuts import render

def chat(request, goods_id, seller_id, buyer_id):
    return render(request, 'chat.html')

def room(request, goods_id, seller_id, buyer_id):
    return render(request, 'chat.html', {
        'goods_id': goods_id,
        'seller_id': seller_id,
        'buyer_id': buyer_id,
    })