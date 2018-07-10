# -*- coding: utf-8 -*-

from models import Article, CmdbCi, CmdbCiIp
from rest_framework import serializers


# Serializers定义了API的表现.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url', 'title', 'content', 'pub_time')


class CmdbciSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CmdbCi
        fields = ('url', 'Location', 'Asset_Status')


# class CiIpSerializer(serializers.HyperlinkedModelSerializer):
class CiIpSerializer(serializers.ModelSerializer):  # 这种情况下显示id而不显示超链接
    class Meta:
        model = CmdbCiIp
        depth = 2
        fields = ('url', 'cmdb_ci', 'Network_Zone')
