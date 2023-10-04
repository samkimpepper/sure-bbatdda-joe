from django.urls import path
from django.contrib.auth import views as auth_views
from ..sure_app_views import views_user

# Create your views here.(
urlpatterns = [
    path('login/',views_user.login_Form,name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views_user.register, name='register'),
    path('location/', views_user.location_auth, name='location'),
    path('set_location/', views_user.set_location, name='set_location'),
    path('set_location_certification/', views_user.set_location_certification, name='set_location_certification'),
]
