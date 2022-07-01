from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model

from django.core.exceptions import ObjectDoesNotExist


from django.http import JsonResponse
from rest_framework import status
# from rest_framework.views import APIView, TokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view  
from rest_framework.response import Response
import jwt

from .serializers import CustomTokenObtainPairSerializer


from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

class InvalidUser(AuthenticationFailed):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = ('Credentials is invalid or expired')
    default_code = 'user_credentials_not_valid'

class InactiveUser(AuthenticationFailed):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_detail = ("Credentials is invalid or didn't match")
    default_code = 'user_inactive'

# class TokenValidate(APIView):
#     permission_classes = (IsAuthenticated,)
#     def get(self, request):
#         content = {"content": "This view is protected"}
#         return Response(content)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['GET'])  
def getRoutes(request): 
    routes = [ 
        '/token',
        '/token/refresh/',
    ]
    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, ])
def authenticate_user(token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return Response(decoded)

@api_view(['GET'])
def getTest(request):
    content = {"test": "This is a test result"}
    return JsonResponse(content)
