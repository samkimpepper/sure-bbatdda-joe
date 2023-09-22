from django.urls import path, include
from . import views
from .sure_app_urls.urls_alarm import urlpatterns as sure_app_alarm_urls 
from .sure_app_urls.urls_chat import urlpatterns as sure_app_chat_urls
from .sure_app_urls.urls_user import urlpatterns as sure_app_user_urls

# from .sure_app_urls.urls_goods import urlpatterns as sure_app_goods_urls

urlpatterns = [
    path('', views.main, name='main'),
    path('searh/', views.search, name='search'),
    
    path('user/', include(sure_app_user_urls)),
    # path('goods/', include(sure_app_goods_urls)),
    
    path('chat/', include(sure_app_chat_urls)),
    path('alarm/', include(sure_app_alarm_urls)),
]