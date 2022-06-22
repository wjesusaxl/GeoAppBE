from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt

class TokenValidate(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {"content": "This view is protected"}
        return Response(content)

@api_view(['GET'])  
def getRoutes(request): 
    routes = [ 
        '/api/token',
        '/api/token/refresh/',
    ]
    return Response(routes)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, ])
def authenticate_user(request, token):
    decoded = jwt.decode(token, options={"verify_signature": False})
    return Response(decoded)

@api_view(['GET'])
def getTest(self,request):
    content = {"test": "This is a test result"}
    return JsonResponse(content)

