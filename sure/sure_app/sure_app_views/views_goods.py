from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ..models import *
from ..models import Goods



#인기 매물 페이지 by 준경
def trade(request):
    goods = Goods.objects.filter(status=False).order_by('-view_cnt')
    print(goods)
    return render(request, 'trade.html', {'goods': goods})

#검색 페이지 by 준경
def search(request):
    keyword = request.GET.get('search', '') 
    results = Goods.objects.filter(
        Q(title__icontains=keyword)     |
        Q(content__icontains=keyword)   |
        Q(location__icontains=keyword)  |
        Q(price__icontains=keyword),
        status=False        
          # 데이터베이스에서 검색
    ).distinct().order_by('-view_cnt','-like_cnt','-chat_cnt')
    return render(request, 'search.html', {'results': results, 'search': keyword})




#매물 상세 페이지 by 준경
def trade_post(request, good_id):
    good = get_object_or_404(Goods, id=good_id)

    if request.method == 'POST': 
        if 'delete-button' in request.POST:
            good.delete()
            return redirect('trade')

    good.view_cnt += 1 
    good.save() 

    return render(request, 'trade_post.html',{ 'good': good})


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
    

#거래후기 by 채림
def trade_review(request):
    return render(request, 'trade_review.html')