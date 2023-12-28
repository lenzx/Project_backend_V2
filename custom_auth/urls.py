from django.contrib import admin
from django.urls import path
from .views import CustomTokenObtainPairView, LogoutView, VerifyTokenView
urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('verify/', VerifyTokenView.as_view(), name='verify'),
]