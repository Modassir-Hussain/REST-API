import requests
import json

def consume():
    id = str(input('Enter id : '))

    BASE_URL = 'http://127.0.0.1:8000/'
    END_POINT = 'api/'
    FINAL_URL = BASE_URL+END_POINT+id
    res = requests.get(BASE_URL+END_POINT+id+'/')
    print(res.status_code)
    print(res.json())
def submit():
    BASE_URL = 'http://127.0.0.1:8000/api/'
    END_POINT = 'postreq/'
    FINAL_URL = BASE_URL+END_POINT
    py_data = {
    'enum':10005,
    'ename':'Lal babu',
    'esal':1000,
    'eaddr':'janipur',
    }
    json_data = json.dumps(py_data)
    res = requests.post(BASE_URL+END_POINT,data=json_data)
    print(res.status_code)
    print(res.json())
if __name__ == '__main__':
    # consume()
    submit()
