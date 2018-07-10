# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article
import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time',)


class CmdbCiAdmin(admin.ModelAdmin):
    list_display = ('Location', 'Asset_Status', 'Alias')


class CmdbCiIpAdmin(admin.ModelAdmin):
    list_display = ('cmdb_ci', 'Network_Zone')


class CmdbCiSoftAdmin(admin.ModelAdmin):
    list_display = ('cmdb_ci', 'TYPE')


admin.site.register(Article, ArticleAdmin)
admin.site.register(models.CmdbCi, CmdbCiAdmin)
admin.site.register(models.CmdbCiIp, CmdbCiIpAdmin)
admin.site.register(models.CmdbCiSoft, CmdbCiSoftAdmin)
