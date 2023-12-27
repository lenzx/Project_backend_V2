from django.contrib import admin
from django.urls import path, include
from .views import CustomTokenObtainPairView, LogoutView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
]