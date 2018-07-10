# -*- coding: utf-8 -*-
# python
from __future__ import unicode_literals
import random
from . import models
from django.http import HttpResponse
# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader
# celery
from blog import tasks
from celery.result import AsyncResult


# 在Django的views中，每一个响应都由一个函数来处理


def index(request):
    articles = models.Article.objects.all()  # all的返回即为一个列表
    return render(request, 'blog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST['title']
    content = request.POST['content']
    article_id = request.POST['article_id']

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
        # return HttpResponseRedirect('index')  # 此处不是templates页面，而是url

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})


def index_mail(request):
    articles = models.Article.objects.all()  # all的返回即为一个列表
    from_email = settings.DEFAULT_FROM_EMAIL
    text_content = '这是一封重要的邮件.'
    html_content = loader.render_to_string(
        'blog/index.html',
        {'articles': articles}
    )
    # html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
    msg = EmailMultiAlternatives('test sent email function', text_content, from_email, ['1115256979@qq.com'])
    msg.attach_alternative(html_content, "text/html")
    # msg.attach_file(".\\blog\\templates\\blog\\index.html")
    msg.send()
    return render(request, 'blog/index.html', {'articles': articles})  # 邮件能够成功发送，页面也能成功跳转


# 计算结果
def celery_call(request):
    randnum = random.randint(0, 1000)
    # t = tasks.mul.apply_async(args=(randnum, 6))
    t = tasks.mul.delay(randnum, 6)
    print 'random', randnum         # print会打印到python manage.py runserver的日志中
    return HttpResponse(t.id)


# 获取结果
# HttpRequest.GET: 一个类似于字典的对象，包含 HTTP GET 的所有参数。详情请参考 QueryDict 对象。
# 访问http://192.168.17.133:9000/crm/celery_result?id=41177118-3647-4830-b8c8-7be76d9819d7, 所以request.GET可以获取到key=id的value
def celery_result(request):
    task_id = request.GET.get('id')
    res = AsyncResult(id=task_id)
    if res.ready():
        return HttpResponse(res.get())
    else:
        return HttpResponse(res.ready())
