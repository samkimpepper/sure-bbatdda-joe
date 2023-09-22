from django.urls import path
from ..sure_app_views import views_chat

# Create your views here.(
urlpatterns = [
    path('', views_chat.chat, name='chat'),
]
