from django.shortcuts import render
from .models import Goods
# Create your views here.
def main(request):
    goods = Goods.objects.order_by('status', '-view_cnt')
    return render(request, 'main.html',{'goods': goods})

def search(request):
    return render(request, 'search.html')