import os, json, requests
from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from enginedb.views import getConfigFile
# from django.contrib.auth.decorators import permission_required

# @permission_required('polls.add_choice', login_url='/loginpage/')
@login_required(login_url='/admin/')
def Home(request):

    domain = ( "https" if request.get_port() == "443" else "http") + "://" + request.get_host()    
    data = {
        "models": getConfigFile("synctool/models"),
        "tasks": getConfigFile("synctool/tasks"),
        "domain": domain,
        "authToken": GetAuthToken(domain)        
    }
    return render(request, "synctool/home.html", data)

def GetAuthToken(basePath):
    token = ""
    conf = getConfigFile("synctool/security")
    authUrl = basePath + "/" + conf["authUrl"]
    response = requests.post(
        url=authUrl,
        headers={
            "Content-Type": "application/json"
        },
        data = json.dumps({
            "email": conf["app-user"],
            "password": conf["app-password"]
        })
    )    

    status = response.status_code
    if status == 200:
        data = json.loads(response.text)
        token = data["data"]["access"]    
    
    return token

def getConfigFile(entry):    
    with open(os.path.join(settings.BASE_DIR, f"static/conf/{entry}.json")) as conf:
        conf = json.load(conf)    
    return conf
