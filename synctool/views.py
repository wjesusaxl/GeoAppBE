from django.shortcuts import render

def Home(request):
    data = {
        "models": ['company']
    }
    return render(request, "synctool/home.html", data)
