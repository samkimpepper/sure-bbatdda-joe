from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ..models import *
from ..models import Goods
from ..forms import GoodsForm
from ..models import Like
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import JsonResponse
from decimal import Decimal

#인기 매물 페이지 by 준경
@login_required
def trade(request):
    goods = Goods.objects.order_by('status', '-view_cnt')
    print(goods)
    return render(request, 'trade.html', {'goods': goods})

#검색 페이지 by 준경
def search(request):
    keyword = request.GET.get('search', '') 
    results = Goods.objects.filter(
        Q(title__icontains=keyword)     |
        Q(content__icontains=keyword)   |
        Q(location__icontains=keyword)  |
        Q(price__icontains=keyword)      # 데이터베이스에서 검색
    ).distinct().order_by('status','-view_cnt','-like_cnt','-chat_cnt')
    return render(request, 'search.html', {'results': results, 'search': keyword})




#매물 상세 페이지 by 준경
@login_required
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
            form = GoodsForm(request.POST, request.FILES, instance=goods)
        else:
            form = GoodsForm(request.POST, request.FILES)

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

    return render(request, 'write.html', {'form': form})
    

# trade_post 좋아요 버튼 by 진혁
@login_required
def like_post(request, good_id):
    if request.user.is_authenticated:
        good = get_object_or_404(Goods, id=good_id)
        user = request.user

        if request.method == 'POST':
            is_liked = request.POST.get('is_liked')
            if is_liked == 'true':
                # 이미 '좋아요'를 눌렀다면 '좋아요' 제거
                Like.objects.filter(goods=good, user=user).delete()
                is_liked = False
            else:
                # '좋아요' 추가
                Like.objects.create(goods=good, user=user)
                is_liked = True

            return JsonResponse({'is_liked': is_liked})
    else:
        return redirect('login')
    
# 게시글 삭제
@login_required
def delete_post(request, good_id):
    good = get_object_or_404(Goods, id=good_id)

    if request.user == good.user:
        good.delete()
        return redirect('trade')
    else:
        return redirect('trade_post', good_id=good.id)

# 거래 완료 by 채림
def complete_trade(request, goods_id):
    if request.method == 'POST':
        goods = get_object_or_404(Goods, id=goods_id)
        goods.status = True 
        goods.save()

        return JsonResponse({'msg': '거래 완료'}, status=200)

#거래후기 by 채림
def trade_review(request):
    if request.method == 'POST':
        data = request.POST
        user = request.user

        buyer = User.objects.get(id=user.id)
        seller = User.objects.get(id=data.get('seller'))

        review = Review.objects.create(
            buyer=buyer,
            seller=seller,
            manner_score=data.get('manner_score'),
            content=data.get('content')
        )

        if review.manner_score == 3:
            seller.manner_tmp += 1
        elif review.manner_score == 2:
            seller.manner_tmp += Decimal(0.5) 
        else:
            seller.manner_tmp -= Decimal(0.5)
            print(seller.manner_tmp)
        seller.save()

        content = f"{buyer.username}님이 후기를 보내셨습니다."
        link = "detail/" + str(review.id) + "/"

        alarm = Alarm.objects.create(user=seller, content=content, link=link)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user{seller.id}", {
                "type": "receive_review",
                "content": content,
                "link": link,
                "alarm_id": alarm.id
            }
        )

        async_to_sync(channel_layer.group_send)(
            f"user{seller.id}", {
                "type": "alarm_cnt",
                "alarm_cnt": Alarm.objects.filter(user=seller.id, is_read=False).count()
            }
        )

        return redirect('review')

    return render(request, 'trade_review.html')


#후기 상세 by 채림
def review_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review_detail.html', {"review":review})


# 매물 정보 가져오기 by 유진
def trade_retrieve(request, goods_id):
    goods = get_object_or_404(Goods, id=goods_id)
    you = get_object_or_404(User, id=goods.user.id)
    
    context = {
        'goods_title': goods.title,
        'goods_img': goods.img.url if goods.img else '',
        'goods_price': goods.price,
        'you_username': you.username,
        'you_manner_tmp': you.manner_tmp
    }
    print(context)
    return JsonResponse(context, safe=False)