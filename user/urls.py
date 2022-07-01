from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from . import views


urlpatterns = [
    path(r'validate/<email>/', views.validateUser, name='validateUser' ),
    # path('getTest/', views.getTest, name='getTest'),
 ]



