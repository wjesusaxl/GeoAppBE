from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('metadata/', include('metadata.urls')),
    path('', include('api.api.urls')),
    path('user/', include('user.urls')),
    path('synctool/', include('synctool.urls')),
    path('dbengine/', include('dbengine.urls')),
]

