from django.urls import path
from ..sure_app_views import views_chat

# Create your views here.(
urlpatterns = [
    path('', views_chat.chat, name='chat'),
    path("<int:goods_id>/<int:seller_id>/<int:buyer_id>", views_chat.room, name="room")
]

