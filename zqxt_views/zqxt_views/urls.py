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
    url(r'^$',calc_views.index,name='index'),
    url(r'^add/(\d*.\d*)/(\d*.\d*)/$', calc_views.add_redirect_to_newadd),
    url(r'^new_add/(\d*.\d*)/(\d*.\d*)/$', calc_views.add2, name='add2'), #正则表达式:add/(\d+)/(\d+)   (\d+)为1个或1个以上的整数  (\d*)可以为任意个整数，包括0个
    url(r'^subtract/(\d*.\d*)/(\d*.\d*)/$',calc_views.subtract,name='subtract'),
    url(r'^multiply/(\d*.\d*)/(\d*.\d*)/$',calc_views.multiply,name='multiply'),
    url(r'^divide/(\d*.\d*)/(\d*.\d*)/$',calc_views.divide,name='divide'),
    url(r'^admin/', admin.site.urls),

]
