# coding:utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/13 17:34'

from .models import Parking
import xadmin
from xadmin import views


class GlobalSetting(object):
    site_title = '智能停车场收费系统后台'
    site_footer = '智能停车场收费系统'
    menu_style = 'accordion'


class ParkingAdmin(object):
    list_display = ['car_plate', 'parking_status', 'order_no', 'in_time',
                    'out_time']
    search_fields = ['car_plate', 'parking_status']
    list_filter = ['car_plate', 'parking_status', 'order_no', 'in_time',
                   'out_time']


xadmin.site.register(Parking, ParkingAdmin)
xadmin.site.register(views.CommAdminView, GlobalSetting)
