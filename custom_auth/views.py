from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from core.settings import base
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken



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

        response = Response({
            'access_token': access_token,
        })

        return response
    
    

class LogoutView(APIView):
    def post(self, request):
        response = Response({"message": "Cierre de sesión exitoso"})
        response.delete_cookie('jwt')
        return response
    
class VerifyTokenView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.data.get('token')

        if not token:
            return Response({'valid': False}, status=400)

        try:
            JWTAuthentication().get_validated_token(token)
            return Response({'valid': True})
        except InvalidToken:
            return Response({'valid': False}, status=400)