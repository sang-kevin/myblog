# -*- coding: utf-8 -*-
from . import models


# 单表操作
def add_ci_default(loc, ali):
    ci1 = models.CmdbCi(Location=loc, Alias=ali)
    ci1.save()


def add_ci(loc, ass, ali):
    ci1 = models.CmdbCi(Location=loc, Asset_Status=ass, Alias=ali)
    ci1.save()


def get_ci_all():
    ci_list = models.CmdbCi.objects.all()
    for var in ci_list:
        print var


def get_ci():
    ci1 = models.CmdbCi.objects.get(pk=3)
    print ci1.Location, ci1.Asset_Status, ci1.Alias


def update_ci():
    models.CmdbCi.objects.filter(id=3).update(Alias='ali20')

    # 也可用来测试级联删除


def delete_ci(nid):
    models.CmdbCi.objects.filter(id=nid).delete()


# 有外键关联的表
def add_ci_ip(ci_id):
    models.CmdbCiIp.objects.create(cmdb_ci_id=ci_id, Network_Zone=1)


def get_ci_ip(nid):
    ip1 = models.CmdbCiIp.objects.filter(id=nid).first()
    if ip1 is None:
        print "id = %d 的数据列不存在" % nid
    else:
        print ip1.id, ip1.Network_Zone, ip1.cmdb_ci_id, ip1.cmdb_ci, ip1.cmdb_ci.id, ip1.cmdb_ci.Location


def update_ci_ip(ip_id):
    models.CmdbCiIp.objects.filter(id=ip_id).update(cmdb_ci_id=3, Network_Zone=2)


def delete_ci_ip(ip_id):
    models.CmdbCiIp.objects.filter(id=ip_id).delete()


def test_save(ci_id):
    test1 = models.CmdbCi.objects.get(id=ci_id)
    test1.Location = "wanted1"
    print test1.Location
    test1.save()
    print test1.Location        # "wanted1" "wanted1"


def test_save2(ci_id):
    test1 = models.CmdbCi.objects.get(id=ci_id)
    test1.Location = "wanted2"
    test2 = models.CmdbCi.objects.get(id=ci_id)
    print test2.Location        # "wanted1"


def test_save3(ci_id):
    test1 = models.CmdbCi.objects.get(id=ci_id)
    test1.Location = "wanted3"
    test1.save()
    test2 = models.CmdbCi.objects.get(id=ci_id)
    print test2.Location        # "wanted3"

    # 结论：save()之前，变量的值改变，但数据库中的值未变
    #       save()之后，数据库中的值改变
