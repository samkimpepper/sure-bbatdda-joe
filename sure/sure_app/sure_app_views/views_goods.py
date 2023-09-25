from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import *
# from ..forms import GoodsForm

#t상품 페이지
def trade_post(request, good_id):
    return render(request, 'trade_post.html')


#인기 매물 페이지
def trade(request):
    return render(request, 'trade.html')


# @login_required
def write(request):
    return render(request, 'write.html')

def search(request):
    return render(request, 'search.html')