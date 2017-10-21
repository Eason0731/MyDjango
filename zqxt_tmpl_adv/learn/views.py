# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ShowString(Request):
    mystring = u'我正在学习Django，用它来建网站'
    return render(Request,'index.html',{'string':mystring})

def ShowList(Request):
    t =["Java","C#","Python","ASP.NET","SQL","Div+Css","Django"]
    return render(Request,'For and List.html',{"TList":t})

def ShowDict(Request):
    info_dict={"site" : u"John学堂" , "content": u"欢迎学习Django"}
    return render(Request,'Dict.html',{'dict': info_dict})

def ShowForAndJudge(Request):
    List = map(str,range(100))
    return render(Request,'Judge.html',{'List':List})


