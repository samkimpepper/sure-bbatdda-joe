from django.urls import path
from django.contrib.auth import views as auth_views
from ..sure_app_views import views_user

# Create your views here.(
urlpatterns = [
    path('login/', views_user.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views_user.register, name='register'),
    path('location/', views_user.location, name='location'),
]
