# -*- coding: utf-8 -*-
# python
from __future__ import unicode_literals
import random
import time
import itchat
from . import models
from django.http import HttpResponse
from io import BytesIO
import base64
# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import loader
# celery
from blog import tasks
from celery.result import AsyncResult

# 数据分析
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


def locations(request):
    """
    Counting device type with pandas
    """
    # df = pd.read_csv('blog/ch02/cmdb_201810051456.csv')  # 该csv文件为db导出
    # Create your engine.
    # dialect+driver://username:password@host:port/database
    engine = create_engine('postgresql://postgres:Hello@2018@localhost/study_db')
    # 不从csv文件中读取DataFrame，而是将SQL数据库表读入DataFrame。
    with engine.connect() as conn, conn.begin():
        df = pd.read_sql_table('cmdb_ci', conn)
    # 数据清洗
    clean_dt = df['Location'].fillna('Missing')     # 填充缺失值(NA/NaN values)
    clean_dt[clean_dt == ''] = 'Unknown'            # 替换空值("")

    # 绘制水平条状图
    dt_counts = clean_dt.value_counts()
    # print(dt_counts)
    # loc1       3
    # loc5       1
    # Unknown    1
    # Name: Location, dtype: int64

    # 如果不直接返给前端图片，代码应该在这里截止，并将Series对象dt_counts转化为python内置的数据格式，然后返回给前端。
    dic = dt_counts.to_dict()
    print dic   # {u'Unknown': 1L, u'loc1': 3L, u'loc5': 1L}
    # 理解：dt_count[:10]: 最多取10个可能的值
    dt_counts[:10].plot(kind='barh', rot=0, title='Location', figsize=(10, 4))

    # 转成图片的步骤
    sio = BytesIO()
    plt.savefig(sio, format='png')
    # 理解这里的.decode()：将str（二进制）decode解码为unicode格式，区别于base64的编解码。
    image_data = base64.b64encode(sio.getvalue()).decode()
    plt.close()  # 记得关闭，不然不同view画出来的图会相互影响
    return render(request, 'blog/location.html', {'image_data': image_data})


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


def login_weixin(request):
    uuid = itchat.get_QRuuid()
    qrStorage = itchat.get_QR(uuid)
    # t = time.strftime("%Y%m%d %H%M%S")
    # response = HttpResponse(qrStorage.getvalue())
    # response['Content-Type'] = 'image/png'
    # response['Content-Disposition'] = 'attachment;filename="QR_%s.png"' % t
    return HttpResponse(itchat.log)


def send_wx_msg(request):
    back = itchat.send_msg('Can you receive?', 'filehelper')
    return HttpResponse(back)
