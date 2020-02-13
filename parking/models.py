# coding:utf-8

from django.db import models
from datetime import datetime


# Create your models here.


class Parking(models.Model):
    """
    停车记录表
    """
    car_plate = models.CharField(max_length=50, null=False, blank=False, verbose_name="车牌号")
    parking_status = models.CharField(max_length=10, choices=(('in', '停车中'), ('out', '已离开')), default='in',
                                      verbose_name='停车状态')
    order_no = models.BigIntegerField(null=True, blank=True, verbose_name='订单号')
    in_time = models.DateField(default=datetime.now, verbose_name='进入时间')
    out_time = models.DateField(verbose_name='离开时间')
    create_time = models.DateField(default=datetime.now, verbose_name='创建时间')
    update_time = models.DateField(verbose_name='更新时间')

    class Meta:
        verbose_name = '停车记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.car_plate


