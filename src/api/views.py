import json
from django.views.generic import View
from django.http import JsonResponse , HttpResponse
from django.core.serializers import serialize
from .models import emp
from api.mixins import SerializeMixin,ResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .utils import is_valid
from .forms import EmployeeForm
@method_decorator(csrf_exempt,name='dispatch')
class JsonCBV(View,SerializeMixin,ResponseMixin):

    def get(self, requset,id, *args, **kwargs,):
        try:
            emp_data = emp.objects.get(id=id)
        except emp.DoesNotExist:
            json_data = json.dumps({'msg':'The Record Is Not Found!'})
            return self.render_to_httpresponse(json_data,400)
            # return HttpResponse(json_data,content_type='application/json',status=404)
        else:
            json_data = self.serialize_data([emp_data,])
            return self.render_to_httpresponse(json_data,200)
            # return HttpResponse(json_data,content_type='application/json',status=200)


    def post(self, requset, *args, **kwargs):
        data = requset.body
        if is_valid(data):
            form = EmployeeForm(json.loads(data))
            print(form.errors)
            if form.is_valid():
                form.save(commit=True)
                json_data = json.dumps({'msg':'Record Saved Successfuly!'})
                return self.render_to_httpresponse(json_data,200)
            if form.errors:
                json_data = json.dumps(form.errors)
            return self.render_to_httpresponse(json_data,400)


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
