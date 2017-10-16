# -*- coding: cp936 -*-
"""zqxt_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from calc import views as calc_views

urlpatterns = [
    url(r'^add/$', calc_views.add, name='add'),
    url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'), #������ʽ:add/(\d+)/(\d+)   (\d+)Ϊ����
    url(r'^subtract/(\d+)/(\d+)/$',calc_views.subtract,name='subtract'),
    url(r'^multiply/(\d+)/(\d+)/$',calc_views.multiply,name='multiply'),
    url(r'^divide/(\d+)/(\d+)/$',calc_views.divide,name='divide'),
    url(r'^admin/', admin.site.urls),

]
