import json
def is_json(myjson):
    try:
        json.loads(myjson)
        return True
    except:
        return False