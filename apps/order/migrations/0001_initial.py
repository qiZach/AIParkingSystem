# Generated by Django 2.0.8 on 2020-02-14 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_no', models.BigIntegerField(blank=True, null=True, verbose_name='订单号')),
                ('car_plate', models.CharField(max_length=50, verbose_name='车牌号')),
                ('order_status', models.CharField(choices=[('1', '已支付'), ('0', '未支付')], default='0', max_length=10, verbose_name='订单状态')),
                ('payment', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='支付金额')),
                ('payment_type', models.CharField(choices=[('1', '支付宝'), ('2', '微信'), ('0', '未支付')], default='0', max_length=10)),
                ('payment_time', models.DateField(verbose_name='支付时间')),
                ('create_time', models.DateField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateField(verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '订单',
                'verbose_name_plural': '订单',
            },
        ),
    ]