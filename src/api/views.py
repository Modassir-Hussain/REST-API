import json
from django.views.generic import View
from django.http import JsonResponse , HttpResponse
from django.core.serializers import serialize
from .models import emp
from api.mixins import SerializeMixin


class JsonCBV(View,SerializeMixin):

    def get(self, requset,id, *args, **kwargs,):
        try:
            emp_data = emp.objects.get(id=id)
        except emp.DoesNotExist:
            json_data = json.dumps({'msg':'The Record Is Not Found!'})
            HttpResponse.status_code=404
        else:
            json_data = self.serialize_data([emp_data,])
            HttpResponse.status_code=200
        return HttpResponse(json_data,content_type='application/json')

    def post(self, requset, *args, **kwargs):
        # emp = {
        #     'Emp No': 1001,
        #     'Emp Name': 'Modassir Hussain',
        #     'Job Title': 'Python Developer',
        #     }
        json_data = json.dumps({'msg':'This is form post'})
        print(json_data)
        return HttpResponse(json_data,content_type='application/json')

    def put(self, requset, *args, **kwargs):
        emp = {
            'Emp No': 1001,
            'Emp Name': 'Modassir Hussain',
            'Job Title': 'Python Developer',
            }
        return JsonResponse(emp)

    def delete(self, requset, *args, **kwargs):
        emp = {
            'Emp No': 1001,
            'Emp Name': 'Modassir Hussain',
            'Job Title': 'Python Developer',
            }
        return JsonResponse(emp)

class Json_list_data(SerializeMixin,View,):
    def get(self,requset,*args,**kwargs):
        try:
            qs = emp.objects.all()

        except emp.DoesNotExist:
            json_data = json.dumps(HttpResponse.status_code)
        else:

            json_data = self.serialize_data(qs)
        return HttpResponse(json_data,content_type='application/json')
