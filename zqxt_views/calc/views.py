# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.core.urlresolvers import reverse #To import reverse
from django.http import HttpResponseRedirect #To import HttpResponseRedirect

# Create your views here.
def index(Request):
    return render(Request,'index.html') #Use render then access to calc/templates/index.html

def add_redirect_to_newadd(Request,a,b):
    return HttpResponseRedirect(reverse('add2', args=(a,b)))
    #The old direct url will return to the new one

def add2(Request,a,b):
    c = float(a) + float(b)
    return HttpResponse(str(c))
    #URL format is:http://127.0.0.1:8000/add/111/333

def subtract(Request,a,b):
    w = float(a) - float(b)
    return HttpResponse((w))
    #URL format is:http://127.0.0.1:8000/subtract/111/333

def multiply(Request,a,b):
    h = float(a) * float(b)
    return HttpResponse(str(h))
    #URL format is:http://127.0.0.1:8000/multiply/111/333

def divide(request,a,b):
    if float(b) == 0:
        return HttpResponse('0 cannot be used as divisor') #判断0不能为除数
    else:
        k = float(a) / float(b)
    return HttpResponse(str(k))
    #URL format is:http://127.0.0.1:8000/divide/111/333




