# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from myadmin.models import Article,Person
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Person,PersonAdmin)
admin.site.register(Article,ArticleAdmin)
