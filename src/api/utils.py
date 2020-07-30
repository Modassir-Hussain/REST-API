import json
def is_valid(data):
    valid = False
    try:
        v_data = json.loads(data)
        valid = True
    except ValueError:
        valid = False
    return valid
