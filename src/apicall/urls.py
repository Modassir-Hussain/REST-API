from django.urls import path, include
from .views import index

app_name = 'apicall'

urlpatterns = [
    path('',index)
]