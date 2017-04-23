import json
import os

def get_movies(data_path):
    try:
        _file_name = "contents.json"
        _file = os.path.join(os.path.abspath(data_path), _file_name)
        with open(_file) as _f:
            return json.load(_f)
    except:
        return None
