from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import *
from ..models import Goods
# from ..forms import GoodsForm

#t상품 페이지
def trade_post(request, good_id):
    return render(request, 'trade_post.html')


#인기 매물 페이지 by 준경
def trade(request):
    posts = Goods.objects.filter(status=False).order_by('view_cnt')
    return render(request, 'trade.html', {'posts': posts})


#글쓰기 페이지 by 진혁
#@login_required
def write(request, goods_id=None):

    if request.method == "POST":
        if goods_id:
            goods = Goods.objects.get(id=goods_id)
        else:
            goods = Goods()

        goods.user = request.user
        goods.title = request.POST.get("title")
        goods.content = request.POST.get("description")
        goods.price = request.POST.get("price")
        goods.location = request.POST.get("location")

        if 'images' in request.FILES:
            goods.img = request.FILES['images']

        goods.save()

        return redirect('trade_post.html')
    else:
        goods = None
        if goods_id:
            goods = Goods.objects.get(id=goods_id)

        return render(request, 'write.html', {'Goods': goods})