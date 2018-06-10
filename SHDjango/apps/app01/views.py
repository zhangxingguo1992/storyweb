from django.shortcuts import render , render_to_response
from django.shortcuts import HttpResponse
# Create your views here.


def hello_world(request):
    import json
    res = {
        'code':200,
        'data':'hello world',
        'message':'ok'
    }
    return HttpResponse(json.dumps(res))