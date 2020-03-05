# coding:utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/14 17:35'

from .models import Order, Charge, Discount
import xadmin


class OrderAdmin(object):
    list_display = ['order_no', 'car_plate', 'order_status', 'payment',
                    'payment_type', 'payment_time', 'create_time']
    search_fields = ['order_no', 'car_plate', 'order_status']
    list_filter = ['order_no', 'car_plate', 'order_status', 'payment',
                   'payment_type', 'payment_time', 'create_time']


class ChargeAdmin(object):
    list_display = ['charge_name', 'pay_level_1', 'pay_level_2', 'pay_level_3',
                    'create_time', 'update_time']


class DiscountAdmin(object):
    list_display = ['discount_name', 'discount', 'start_time', 'end_time',
                    'create_time', 'update_time']
    search_fields = ['discount_name', 'discount']
    list_filter = ['discount_name', 'discount', 'start_time', 'end_time',
                   'create_time', 'update_time']


xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(Charge, ChargeAdmin)
xadmin.site.register(Discount, DiscountAdmin)
