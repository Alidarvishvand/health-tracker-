from django.urls import path
from .views import register, user_login, profile, logout
from accounts.api.views import UserRegistrationAPIView, UserDetailAPIView


urlpatterns = [
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('profile/',profile,name='profile'),
    path('logout',logout,name='logout'),

    path('api/register/',UserRegistrationAPIView.as_view(),name='api-register'),
    path('api/user/<int:pk>/',UserDetailAPIView.as_view(),name='api-user-detail'),
]
