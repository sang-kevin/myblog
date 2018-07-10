# -*- coding: utf-8 -*-

from rest_framework import routers
from django.conf.urls import url, include
from blog import rest_views

# Routers 提供了一种简单途径，自动地配置了URL。
router = routers.DefaultRouter()
router.register(r'users', rest_views.UserViewSet)
router.register(r'cmdbcis', rest_views.CmdbciViewSet)
router.register(r'cmdbciips', rest_views.CiIpViewSet)

# 使用自动的URL路由，让我们的API跑起来。
# 此外，我们也包括了登入可视化API的URLs。
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
