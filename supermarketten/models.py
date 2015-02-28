# -*- coding: utf-8 -*-

from django.db import models
import datetime
import traceback
import pytz


class Type(models.Model):
    name = models.CharField(max_length=255, blank=True , null=True)
    info = models.CharField(max_length=255, blank=True , null=True)

    def products(self):
        return Product.objects.filter(type=self)


class Product(models.Model):
    sn = models.CharField(max_length=255, blank=True , null=True)
    type = models.ForeignKey(Type)
    name = models.CharField(max_length=255, blank=True , null=True)
    info = models.CharField(max_length=1024, blank=True , null=True)
    details = models.CharField(max_length=10000, blank=True , null=True)
    price = models.FloatField(default=10.0)
    pic = models.CharField(max_length=255, blank=True , null=True)

    def get_price(self, ap):
        return self.price + int(ap)


class Order(models.Model):
    sn = models.CharField(max_length=255, blank=True , null=True)
    name = models.CharField(max_length=255, blank=True , null=True)
    address = models.CharField(max_length=255, blank=True , null=True)
    phone = models.CharField(max_length=255, blank=True , null=True)
    status = models.IntegerField(default=0)
    urge = models.IntegerField(default=0)
    email = models.CharField(max_length=255, blank=True , null=True)
    time = models.DateTimeField(default=datetime.datetime.now())

    def boms(self):
        return Bom.objects.filter(order=self)

    def total(self):
        total = 0
        for b in self.boms():
            price = b.product.price * b.quantity
            total += price
        return total


    def status_name(self):
        if self.status == 0:
            return u"不显示"
        if self.status == 1:
            return u"已下单"
        if self.status == 2:
            return u"配送中"
        if self.status == 3:
            return u"已完成"
        if self.status == -1:
            return u"已取消"
        return ""

    def next_step(self):
        if self.status == 1:
            return u"发货"
        if self.status == 2:
            return u"完成"
        return ""


class Bom(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)


class Comment(models.Model):
    product = models.ForeignKey(Product)
    content = models.CharField(max_length=1024, blank=True , null=True)
    user = models.CharField(max_length=255, blank=True , null=True)
    time = models.DateTimeField(default=datetime.datetime.now())

    def friendly_time(self):
        nowtime = datetime.datetime.now(pytz.utc)
        msgtime = self.time
        print msgtime
        print nowtime
        try:
            a = nowtime - msgtime
        except:
            traceback.print_exc()
        if (nowtime - msgtime).days == 0:
            differ_seconds = (nowtime - msgtime).seconds
            if differ_seconds < 3600:
                return str(differ_seconds / 60) + u"分钟前"
            else:
                return str(differ_seconds / 3600) + u"小时前"
        elif (nowtime - msgtime).days == 1:
            return u"昨天"
        elif (nowtime - msgtime).days == 2:
            return u"前天"
        else:
            return str((nowtime - msgtime).days) + u"天前"


