from django.urls import path, include
from . import views
from .sure_app_urls.urls_alarm import urlpatterns as sure_app_alarm_urls 
from .sure_app_urls.urls_chat import urlpatterns as sure_app_chat_urls
from .sure_app_urls.urls_user import urlpatterns as sure_app_user_urls
from .sure_app_urls.urls_goods import urlpatterns as sure_app_goods_urls
from django.conf import settings
from django.conf.urls.static import static

app_name = ""

urlpatterns = [
    path('', views.main, name='main'),
    path('searh/', views.search, name='search'),
    
    path('user/', include(sure_app_user_urls)),
    path('goods/', include(sure_app_goods_urls)),
    
    path('chatting/', include(sure_app_chat_urls)),
    path('alarm/', include(sure_app_alarm_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
