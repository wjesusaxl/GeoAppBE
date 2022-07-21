import os, json, requests
from django.http import HttpResponse, JsonResponse
from django.conf import settings

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.exceptions import APIException

from dbengine.views import getConfigFile
# from django.contrib.auth.decorators import permission_required

# @permission_required('polls.add_choice', login_url='/loginpage/')

@login_required(login_url='/admin/')
def Home(request):

    domain = ( "https" if request.get_port() == "443" else "http") + "://" + request.get_host()    
    data = {
        "models": getConfigFile("synctool/metadata/models"),
        "tasks": normalizeDict(getConfigFile("synctool/tasks")),
        "domain": domain,
        "authToken": GetAuthToken(domain)        
    }
    return render(request, "synctool/home.html", data)

def GetAuthToken(basePath):
    token = ""
    authConf = getConfigFile("synctool/app-authentication")
    authUrl = basePath + "/" + authConf["authUrl"]
    response = requests.post(
        url=authUrl,
        headers={
            "Content-Type": "application/json"
        },
        data = json.dumps({
            "email": authConf["appAuthUser"],
            "password": authConf["appAuthPassword"]
        })
    )    

    status = response.status_code
    if status == 200:
        data = json.loads(response.text)
        token = data["data"]["access"]    
    
    return token

def normalizeDict(dict):    
    result = []
    for k in dict.keys():
        item = dict[k]
        if not "code" in item:
            item["code"] = k
            result.append(item)
    return result

def getConfigFile(entry):    
    with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
        conf = json.load(conf)    
    return conf

