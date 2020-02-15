# coding:utf-8

import datetime
from django.shortcuts import render, redirect, HttpResponse

from .models import Order
from parking.models import Parking
from utils.pay import AliPay


# Create your views here.

def show_msg(request):
    if request.method == 'GET':
        alipay = AliPay(
            appid="2016080900196363",  # APPID
            app_notify_url='http://zhangsiqi.natapp1.cc/check_order/',
            # 支付宝会向这个地址发送post请求
            return_url='http://zhangsiqi.natapp1.cc/show_msg/',
            # 支付宝会向这个地址发送get请求
            app_private_key_path='keys/app_private_2048.txt',  # 应用私钥
            alipay_public_key_path='keys/alipay_public_2048.txt',  # 支付宝公钥
            debug=True,  # 默认是False
        )
        params = request.GET.dict()  # 获取请求携带的参数并转换成字典类型
        sign = params.pop('sign', None)  # 获取sign的值
        # 对sign参数进行验证
        status = alipay.verify(params, sign)
        if status:
            return render(request, 'show_msg.html', {'msg': '支付成功'})
        else:
            return render(request, 'show_msg.html', {'msg': '支付失败'})
    else:
        return render(request, 'show_msg.html', {'msg': '只支持GET请求，不支持其它请求'})


def check_order(request):
    """
    支付宝通知支付的结果信息，如果支付成功可以用来修改订单的状态
    :param request:
    :return:
    """
    print('check_order be called.')
    if request.method == 'POST':
        alipay = AliPay(
            appid="2016080900196363",  # APPID
            app_notify_url='http://zhangsiqi.natapp1.cc/check_order/',
            # 支付宝会向这个地址发送post请求
            return_url='http://zhangsiqi.natapp1.cc/show_msg/',
            # 支付宝会向这个地址发送get请求
            app_private_key_path='keys/app_private_2048.txt',  # 应用私钥
            alipay_public_key_path='keys/alipay_public_2048.txt',  # 支付宝公钥
            debug=True,
        )
        body_str = request.body.decode('utf-8')  # 转成字符串
        from urllib.parse import parse_qs
        post_data = parse_qs(body_str)  # 根据&符号分割
        # print(post_data)  # post_data是一个字符串
        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        if status:  # 支付成功
            # 获取订单号
            out_trade_no = post_dict['out_trade_no']
            Order.objects.filter(order_no=int(out_trade_no)).update(
                order_status='1',
                payment_type='1',
                payment_time=datetime.datetime.now())
            return HttpResponse('success')  # 向支付宝返回success,表示接收到请求
        else:
            return HttpResponse('支付失败')
    else:
        return HttpResponse('只支持POST请求')
