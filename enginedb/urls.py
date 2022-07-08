from django.urls import path
from . import views

urlpatterns = [    
    # path(r'entity/<entity>/values', views.getValues, name='getValues' ),
    path('entity/<keyspace>/<entity>/<id>', views.Entity.as_view(), name='entity' ),
    path('getCSRFToken', views.getCSRFToken, name='getCSRFToken'),
    path('sync/<from>/<to>', views.Synchronization.as_view(), name='synchronization')
]