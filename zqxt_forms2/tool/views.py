# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import AddForms
# Create your views here.

from django.http import HttpResponse

def Index(request):
    if request.method == 'POST':
        form = AddForms(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        form = AddForms()

    return render(request,'Index.html',{'form':form})
