from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ..models import *
from ..models import Goods
from ..forms import GoodsForm


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
def write(request, good_id=None):
    if request.method == "POST":
        if good_id:  
            goods = get_object_or_404(Goods, id=good_id)
            form = GoodsForm(request.POST or None, request.FILES or None, instance=goods)
        else:  
            form = GoodsForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            goods = form.save(commit=False)
            goods.user = request.user
            goods.save()
            
            return redirect('trade_post', good_id=goods.id) 

    else:  
        if good_id:
            goods = get_object_or_404(Goods, id=good_id)
            form = GoodsForm(instance=goods)
        else:
            form = GoodsForm()

    return render(request,'write.html',{'form':form})
    

# trade_post 좋아요 버튼 by 진혁
def like_post(request, good_id):
    if request.user.is_authenticated:
        good = get_object_or_404(Goods, id=good_id)
        user = request.user

        if Like.objects.filter(goods=good, user=user).exists():
            # 이미 '좋아요'를 눌렀다면 '좋아요' 제거
            Like.objects.filter(goods=good, user=user).delete()
        else:
            # '좋아요' 추가
            Like.objects.create(goods=good, user=user)

        return redirect('trade_post', good_id=good.id)
    else:
        return redirect('login')


#거래후기 by 채림
def trade_review(request):
    return render(request, 'trade_review.html')
