# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import generics
from blog import models, serializer


# ViewSets 定义了 视图（view） 的行为.
class UserViewSet(viewsets.ModelViewSet):
    queryset = models.Article.objects.all()
    serializer_class = serializer.UserSerializer


class CmdbciViewSet(viewsets.ModelViewSet):
    queryset = models.CmdbCi.objects.all()
    serializer_class = serializer.CmdbciSerializer
    # serializer_class = serializer


class CiIpViewSet(viewsets.ModelViewSet):
    queryset = models.CmdbCiIp.objects.all()
    serializer_class = serializer.CiIpSerializer
