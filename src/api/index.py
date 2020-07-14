import requests
import json

def consume():
    id = str(input('Enter id : '))
    BASE_URL = 'http://127.0.0.1:8000/'
    END_POINT = 'api/'
    FINAL_URL = BASE_URL+END_POINT+id
    # print('FINAL_URL------>',FINAL_URL)
    res = requests.get(BASE_URL+END_POINT+id+'/')
    print(res.json())
if __name__ == '__main__':
    consume()
