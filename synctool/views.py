from django.shortcuts import render

def Home(request):

    data = {
        "models": ['User'],
        "domain": ( "https" if request.get_port() == "443" else "http") + "://" + request.get_host()
    }
    return render(request, "synctool/home.html", data)
