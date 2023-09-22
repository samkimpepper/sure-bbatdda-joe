from django.urls import path
from ..sure_app_views import views_user

# Create your views here.(
urlpatterns = [
    path('login', views_user.login, name='login'),
]
