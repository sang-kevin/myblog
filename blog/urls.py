from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^index/$', views.index_mail),
    url(r'^api/', include('blog.rest_urls')),
    url(r'^article/(?P<article_id>\d+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>\d+)$', views.edit_page, name='edit_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
    url(r'^celery_call/$', views.celery_call),
    url(r'^celery_result$', views.celery_result)
]
