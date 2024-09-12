from  django.urls import path, include
from . import views 

urlpatterns = [
    path('register/',views.RgisterApiViews.as_view(),name="register"),
    path('token/login/',views.CustomObtainAuthToken.as_view(),name="token-login"),
]
