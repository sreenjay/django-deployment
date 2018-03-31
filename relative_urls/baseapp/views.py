from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return render(req, "baseapp/index.html")

def base(req):
    return render(req, "baseapp/base.html")

def other(req):
    return render(req, "baseapp/other.html")

def relative(req):
    return render(req, "baseapp/relative_url_templates.html")
