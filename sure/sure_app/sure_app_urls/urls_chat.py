from django.urls import path
from ..sure_app_views import views_chat

# Create your views here.(
urlpatterns = [
    path('', views_chat.chatting, name='chatting'),
    path('<int:goods_id>/<int:you_id>', views_chat.chatting, name='chatting_and_chat_id'),
    path('messages/<int:chat_id>', views_chat.messages, name='messages'),
]

