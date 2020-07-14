from api import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('<int:id>/',views.JsonCBV.as_view(),name='JsonCBV'),
    path('all/', views.Json_list_data.as_view(),name='Json_list_data')
]
