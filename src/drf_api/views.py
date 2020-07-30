# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from drf_api.models import Employee
# from drf_api.serializers import EmployeeModelSerializer
# from rest_framework import status
# from django.http import Http404
# from rest_framework.decorators import api_view, APIView
# from rest_framework.response import Response

# @api_view(['GET','POST'])
# def emplist(request, format = None):
#     if request.method == 'GET':
#         allEmp = Employee.objects.all()
#         serializer = EmployeeSerializers(allEmp,many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         print('-------data--------',data)
#         serializer = EmployeeSerializers(data = data)
#         print('------serializers-------',serializer)
#         if serializer.is_valid():
#             serializer.save()
#             # return JsonResponse(serializer.data, status=200)
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         # return JsonResponse(serializer.errors, status=400)
#         print("-----errors------->",serializer.errors)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
# @api_view(['GET','PUT','DELETE'])
# def employee_detail(request, pk,format = None):
#     """
#     Retrieve, update or delete a code Employee.
#     """
#     try:
#         emp = Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = EmployeeSerializers(emp)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EmployeeSerializers(emp, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class EmpolyeeList(APIView):

#     """
#     This is class based view
#     """
#     def get(self, request, format = None):

#         allEmp = Employee.objects.all()
#         serializer = EmployeeModelSerializer(allEmp,many=True)
#         print('------serializers-------',serializer)
#         return Response(serializer.data)

#     def post(self, request, format = None):

#         data = JSONParser().parse(request)
#         serializer = EmployeeModelSerializer(emp, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, format = None):
#         emp.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class EmployeeDetails(APIView):


#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise   Http404

#     def get(self, request, pk, format = None):

#         emp = self.get_object(pk)
#         serializer = EmployeeModelSerializer(emp)
#         return Response(serializer.data)

#     def put(self, request, format=None):

#         emp  = self.get_object(pk)
#         serializer = EmployeeModelSerializer(emp, data=request.data)

    
'''-----------------------------------------------------------------------------------------------------------------'''

from drf_api.models import Employee
from drf_api.serializers import EmployeeModelSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import authentication
from drf_api.permissions import IsOwnerOrReadOnly
from django.conf import settings
from rest_framework import viewsets


class EmployeeViewset(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list` and `detail` actions.
    """

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # authentication_classes = [authentication.TokenAuthentication,]


    # queryset  = Employee.objects.filter(ename__startswith='m')|Employee.objects.filter(ename__endswith='n')
    queryset = Employee.objects.all()
    

    print(queryset.query)
    serializer_class = EmployeeModelSerializer



class UserViewset(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
    # authentication_classes = [authentication.TokenAuthentication,]

    queryset = User.objects.all()
    serializer_class = UserSerializer

