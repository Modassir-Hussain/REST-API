from django.core.serializers import serialize
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
