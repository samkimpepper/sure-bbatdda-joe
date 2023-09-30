from django.urls import path
from ..sure_app_views import views_chat

# Create your views here.(
urlpatterns = [
    path('', views_chat.chatting, name='chatting'),
    path('<int:chat_id>', views_chat.chatting, name='chatting'),
    path('messages/<int:chat_id>', views_chat.messages, name='messages'),
]

