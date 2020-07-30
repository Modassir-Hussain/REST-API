from django.core.serializers import serialize
from django.http import HttpResponse
import json
class SerializeMixin(object):
    def  serialize_data(self,qs):

        json_data = serialize('json',qs)
        pdict = json.loads(json_data)
        final_list = []
        for obj in pdict:
            final_list.append(obj['fields'])
        json_data = json.dumps(final_list)
        return json_data
class  ResponseMixin(object):

    def render_to_httpresponse(self,json_data,code,*args,**kwargs):
        response = HttpResponse(json_data,content_type='application/json',status=code)
        return response
