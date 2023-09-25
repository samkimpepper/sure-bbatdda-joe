from django.urls import path
from ..sure_app_views import views_goods

# Create your views here.(
urlpatterns = [
    # path('trade_post', views_goods.trade_post, name='trade_post'),
    path('trade', views_goods.trade, name='trade'),
    path('trade_post/<int:good_id>/',views_goods.trade_post,name='trade_post'),
    path('write', views_goods.write, name='write'),
]