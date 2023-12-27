from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from core.settings import base


class CustomTokenObtainPairView(APIView):
    permission_classes = [AllowAny]  

    def get_serializer(self, *args, **kwargs):
        return TokenObtainPairSerializer(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        User = get_user_model()
        user = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        response = Response({'message': 'Inicio de sesión exitoso'})
        access_lifetime = base.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']
        max_age =  access_lifetime.total_seconds()
        print(max_age)
        response.set_cookie('jwt', access_token, domain='.localhost',max_age=max_age, httponly=True)
        return response
    
    

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Cierre de sesión exitoso"})
        response.delete_cookie('jwt')
        return response