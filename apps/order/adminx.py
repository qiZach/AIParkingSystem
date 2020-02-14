# coding:utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/14 17:35'

from .models import Order
import xadmin


class OrderAdmin(object):
    list_display = ['order_no', 'car_plate', 'order_status', 'payment',
                    'payment_type', 'payment_time', 'create_time']
    search_fields = ['order_no', 'car_plate', 'order_status']
    list_filter = ['order_no', 'car_plate', 'order_status', 'payment',
                   'payment_type', 'payment_time', 'create_time']


xadmin.site.register(Order, OrderAdmin)
