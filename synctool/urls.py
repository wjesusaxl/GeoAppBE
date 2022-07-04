from django.urls import path
from .views import Home
from . import views

urlpatterns = [
    path('', Home, name = 'Home'),
]