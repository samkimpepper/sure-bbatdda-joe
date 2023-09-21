from django.urls import path, include
from ..sure_app_views import views_alarm

urlpatterns = [
    path('', views_alarm.index, name='index'),
]