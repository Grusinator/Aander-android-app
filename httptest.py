import httplib2 as http
import json


def trygetdata():
    try:
        from urlparse import urlparse
    except ImportError:
        from urllib.parse import urlparse

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8'
    }

    uri = 'http://localhost:8000'
    path = '/adventures/'

    target = urlparse(uri+path)
    method = 'GET'
    body = ''

    h = http.Http()

    # If you need authentication some example:
    #if auth:
    #    h.add_credentials(auth.user, auth.password)

    response, content = h.request(
            target.geturl(),
            method,
            body,
            headers)

    # assume that content is a json reply
    # parse content with the json module
    data = json.loads(content)

    print data
    for elm in data:

        print elm['title']
        print elm['description']

def trylogin():
    try:
        from urlparse import urlparse
    except ImportError:
        from urllib.parse import urlparse

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json; charset=UTF-8'
    }

    uri = 'http://localhost:8000'
    path = '/login/'

    target = urlparse(uri + path)
    method = 'POST'
    body = ''

    h = http.Http()



    h.add_credentials("grusinator", "test1234")

    response, content = h.request(
        target.geturl(),
        method,
        body,
        headers)

    # assume that content is a json reply
    # parse content with the json module

    print content

    data = json.loads(content)

    print data
    # for elm in data:
    #     print elm['title']
    #     print elm['description']


if __name__ == "__main__":
    trylogin()