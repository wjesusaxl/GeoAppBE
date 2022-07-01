from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


import user
from .models import User
from django.core import serializers

# Create your views here.

def validateUser(request, email):
    result = {
        "operation" : "user-validation",
        "data": None
    }
    
    users = User.objects.filter(email=email).values('id', 'username', 'email')

    try:

        if not users:
            raise User.DoesNotExist

        result["data"] = users[0]
        return returnResult(result)

    except User.DoesNotExist:        
        return returnResult(result, "404", False, 404)

def returnResult(result, code="200", success=True, status=200):
    result["code"] = code
    result["success"] = success
    return JsonResponse(result, status=status)




    