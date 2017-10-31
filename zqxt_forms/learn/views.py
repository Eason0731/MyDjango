# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.urlresolvers import reverse
# Create your views here.

def Home(request):
    return render(request,'Home.html')

def Add(Request):
    a = Request.GET['a']
    b = Request.GET['b']
    return HttpResponse(str(int(a) + int(b)))
