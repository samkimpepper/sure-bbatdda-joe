from django.urls import path
from ..sure_app_views import views_goods

# Create your views here.(
urlpatterns = [
    # path('trade_post', views_goods.trade_post, name='trade_post'),
    path('trade', views_goods.trade, name='trade'),
    path('trade_post/<int:good_id>/',views_goods.trade_post,name='trade_post'),
    path('write', views_goods.write, name='write'),
    path('search', views_goods.search, name='search'),
    path('trade/review/', views_goods.trade_review, name='review'),
    path('write/<int:good_id>/', views_goods.write,name='edit'),   # 수정 시 URL 
    path('write/', views_goods.write,name='write'),  # 새 글 작성 시 URL 
    path('like/<int:good_id>/', views_goods.like_post, name='like_post'),#좋아요 기능
    path('trade/review/detail/<int:review_id>/', views_goods.review_detail, name='review-detail'), #후기 상세
    path('trade_post/retrieve/<int:goods_id>/', views_goods.trade_retrieve, name='trade_retrieve'), # goods_id에 해당하는 매물 정보 가져오기
    path('delete/<int:good_id>/', views_goods.delete_post, name='delete_post'),#게시글 삭제
]
