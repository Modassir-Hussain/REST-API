from django.urls import path
from drf_api.views import EmployeeViewset,UserViewset
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'drf_api'


Employee_List = EmployeeViewset.as_view({
    'get': 'list',
    'post': 'create'

})
Employee_Details = EmployeeViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

User_List = UserViewset.as_view({
    'get': 'list',
    'post': 'create'

})
User_Details = UserViewset.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    # path('', api_root),
    path('employee/',Employee_List, name='Employee-List'),
    path('employee/<int:pk>/', Employee_Details, name='Employee-Details'),
    path('user/', User_List, name='User-List'),
    path('user/<int:pk>/', User_Details, name='User-Details'),
   
]


urlpatterns = format_suffix_patterns(urlpatterns)


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from drf_api import views

# app_name = 'drf_api'

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'employee', views.EmployeeViewset)
# router.register(r'employee/<int:pk>', views.EmployeeDetails)

# # The API URLs are now determined automatically by the router.
# urlpatterns = [
#     path('', include(router.urls)),
# ]