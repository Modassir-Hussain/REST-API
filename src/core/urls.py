from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls',namespace='api')),
    path('drf/',include('drf_api.urls',namespace='drf_api')),
    path('apicall/',include('apicall.urls',namespace='apicall')),
    path('api-auth/', include('rest_framework.urls')),
    
]
