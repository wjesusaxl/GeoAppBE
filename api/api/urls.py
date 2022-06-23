from django.urls import path
from . import views
#from api.api.core import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', views.getRoutes),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('getTest/', views.getTest, name='getTest')
 ]
