# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def Index(Request):
    return render(Request,'Index.html')

def JudgeNumOne(request):
    num = 88
    return render(request,'JudgeNumber1.html',{'myNum':num})

def JudgeNumTwo(Request):
    num = 94
    return render(Request,'JudgeNumber2.html',{'myNum2':num})

def JudgeString(request):
    List = ["McLaren","Ferrari","Mercedes","Williams","Red Bull"]
    return render(request,'JudgeString.html',{'myList':List})
