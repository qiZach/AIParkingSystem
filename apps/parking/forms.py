# coding:utf-8
__author__ = 'zhangsiqi'
__date__ = '2020/2/15 16:07'

from django import forms


class IdentifyForm(forms.Form):
    car_plate = forms.CharField(required=True)
