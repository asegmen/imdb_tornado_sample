import urllib
import json
import requests

#return content json
def get_content_by_title(title):
    base_url = "http://omdbapi.com/?t=%s" % title

    response = requests.get(base_url)
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return json.loads(None)


