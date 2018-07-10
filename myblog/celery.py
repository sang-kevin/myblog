# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# 设置Django的环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myblog.settings')

# 设置app的默认处理方式,如果不设置默认是rabbitMQ
app = Celery('myblog',
             broker='redis://localhost',
             backend='redis://localhost'
             )

# 配置前缀
app.config_from_object('django.conf:settings')

# 自动扫描app下的tasks文件
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
