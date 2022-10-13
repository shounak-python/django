from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myview(request):
    num_visits = request.session.get("num_visits",0)+1
    request.session["num_visits"] = num_visits
    resp = HttpResponse(f"view count={num_visits}")
    resp.set_cookie('dj4e_cookie', '6764e7a4', max_age=1000)
    return resp

def owner(request):
    return HttpResponse("Hello, world. 0e989f4a is the polls index. 6764e7a4 ")
