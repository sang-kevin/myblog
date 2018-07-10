# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    content = models.TextField(null=True)
    pub_time = models.TimeField(null=True)

    def __unicode__(self):
        return self.title


class TestA(models.Model):
    name = models.CharField(max_length=32, default='')


class TestB(TestA):
    desc = models.CharField(max_length=32, default='')


class TestC(models.Model):
    info = models.CharField(max_length=32, default='')
    test_a = models.ForeignKey('TestA', related_name='related', on_delete=models.CASCADE)


# 有些字段类型实现时可能需要进行些调整，RAM， DISK等使用integer类型， warranty start 和 end可能更适用于datetime类型。
class CmdbCi(models.Model):
    ASSET_STATUS_CHOICES = (
        (1, 'Decommissioned'),  # 第一个参数是真正的model参数，#第二个参数则是方便人们理解阅读
        (2, 'Deactive'),
        (3, 'Active'),
        (4, 'Implementing'),
        (5, 'Not owned by DXC'),
    )

    APP_CATEGORY_CHOICES = (
        (1, 'LEWTAN'),
        (2, 'MFT'),
        (3, 'Security'),
        (4, 'Jump for VPN'),
        (5, 'BPODAT'),
        (6, 'VMware'),
        (7, 'Core Service'),
        (8, 'BUR'),
        (9, 'WSCP'),
        (10, 'POC'),
        (11, 'RTA'),
        (12, 'IMAGING'),
        (13, 'SOD'),
        (14, 'LAN localization'),
        (15, 'Jump Server for DXC Hosting'),
        (16, 'DRIS'),
        (17, 'AES Server'),
        (18, 'CARRS'),
        (19, 'Test'),
        (20, 'RTCS'),
        (21, 'Exchange Upgrade POC'),
        (22, 'SIEM'),
        (23, 'SVN'),
        (24, 'HRIS'),
        (25, 'WAF'),
    )

    Location = models.CharField(max_length=255)
    Asset_Status = models.IntegerField(choices=ASSET_STATUS_CHOICES, default=1)
    # Environment = models.CharField(max_length=255, null=True)
    # Hostname = models.CharField(max_length=255)
    Alias = models.CharField(max_length=255, null=True)

    # Domain = models.CharField(max_length=255, null=True)
    # Physical_Host_Name = models.CharField(max_length=255, null=True)
    # Server_Role = models.CharField(max_length=255)
    # App_Category = models.IntegerField(choices=APP_CATEGORY_CHOICES)
    # AV_required = models.CharField(max_length=32, null=True)
    # Cluster_Name = models.CharField(max_length=255, null=True)
    # Cluster_Type = models.CharField(max_length=255, null=True)
    # Virtual_IP = models.GenericIPAddressField(null=True)
    # Heartbeat_IP = models.GenericIPAddressField(null=True)
    # Serverity = models.CharField(max_length=255, null=True)
    # Cluster_Serverity = models.CharField(max_length=255, null=True)
    # Server_Port = models.CharField(max_length=255, null=True)
    # Switch_Name = models.CharField(max_length=255, null=True)
    # Switch_Port = models.CharField(max_length=32, null=True)
    # Power_Redundancy = models.CharField(max_length=255, null=True)
    # Rack_Location = models.CharField(max_length=255, null=True)
    # U = models.CharField(max_length=255, null=True)
    # Warranty_Start = models.DateTimeField(null=True)
    # Warranty_End = models.DateTimeField(null=True)
    # CPU = models.IntegerField(max_length=32, null=True)
    # RAM = models.IntegerField(max_length=32, null=True)
    # Disk_Config = models.IntegerField(max_length=32, null=True)
    # Application_Owner = models.CharField(max_length=255, null=True)
    # Contact_Phone = models.CharField(max_length=32, null=True)
    # Contact_Mail = models.EmailField(max_length=254, null=True)
    # Remark = models.CharField(max_length=255, null=True)
    # Decommissioning_Initial_Date = models.DateTimeField(null=True)
    # CCR_ID = models.CharField(max_length=255, null=True)
    # Special_Reboot_Procedure = models.CharField(max_length=255, null=True)
    # Remark9 = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'cmdb_ci'


class CmdbCiIp(models.Model):
    NETWORK_ZONE_CHOICES = (
        (1, 'Infra zone'),
        (2, 'APP/DB zone'),
        (3, 'Web zone'),
    )
    cmdb_ci = models.ForeignKey('CmdbCi', on_delete=models.CASCADE)
    # TYPE = models.CharField(max_length=32)
    # Biz_IP = models.GenericIPAddressField(null=True)
    # VLAN = models.CharField(max_length=255, null=True)
    # Server_Port = models.CharField(max_length=255, null=True)
    # Switch_Name = models.CharField(max_length=255, null=True)
    # Switch_Port = models.CharField(max_length=32, null=True)
    Network_Zone = models.IntegerField(choices=NETWORK_ZONE_CHOICES, default=1)

    # Mgmt_IP = models.GenericIPAddressField(null=True)
    # VLAN2 = models.CharField(max_length=255, null=True)
    # Interface = models.CharField(max_length=255, null=True)
    # Switch_Name3 = models.CharField(max_length=255, null=True)
    # Switch_Port4 = models.CharField(max_length=32, null=True)
    # iLO_Name = models.CharField(max_length=255, null=True)
    # Backup_IP = models.GenericIPAddressField(null=True)
    # VLAN5 = models.CharField(max_length=32, null=True)
    # Server_Port6 = models.CharField(max_length=32, null=True)
    # Switch_Name7 = models.CharField(max_length=255, null=True)
    # Switch_Port8 = models.CharField(max_length=32, null=True)
    # OOB_IP = models.GenericIPAddressField(null=True)
    # Other_IP = models.GenericIPAddressField(null=True)
    # Internet_IP = models.GenericIPAddressField(null=True)
    # Internet_Domain_Name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'cmdb_ci_ip'


class CmdbCiSoft(models.Model):
    OS_TYPE_CHOICES = (
        (1, 'WINDOWS'),
        (2, 'LINUX'),
        (3, 'ESX'),
    )
    Operating_System_CHOICES = (
        (1, 'Microsoft Windows 7 (32-bit)'),
        (2, 'Microsoft Windows 7 (64-bit)'),
        (3, 'LINUX RedHat EL 6.7 64bit'),
        (4, 'Novell SUSE Linux Enterprise 11 (64-bit)'),
        (5, 'Windows 7'),
        (6, 'Windows 7 x64'),
        (7, 'Microsoft Windows Server 2012 R2 (64-bit)'),
        (8, 'Other Linux (64-bit)'),
        (9, 'Windows 10'),
        (10, 'Microsoft Windows Server 2008 R2 (64-bit)'),
        (11, 'LINUX RedHat EL 5.8'),
        (12, 'VMware ESXi, 6.0.0, 4192238'),
        (13, 'Microsoft Windows Server 2003 Standard'),
    )
    cmdb_ci = models.ForeignKey('CmdbCi', on_delete=models.CASCADE)
    TYPE = models.CharField(max_length=32, null=True)

    OS_Type = models.IntegerField(choices=OS_TYPE_CHOICES, default=1)

    # Operating_System = models.IntegerField(choices=Operating_System_CHOICES, default=1)
    # DB_Type = models.CharField(max_length=32, null=True)
    # DB_Version = models.CharField(max_length=32, null=True)
    # DB_Instance = models.CharField(max_length=255, null=True)
    # DB_Instance_Name = models.CharField(max_length=255, null=True)
    # Middleware_Version = models.CharField(max_length=32, null=True)
    # Instance = models.CharField(max_length=255, null=True)
    # Instance_Name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'cmdb_ci_soft'
