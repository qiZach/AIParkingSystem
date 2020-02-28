# Generated by Django 2.0.8 on 2020-02-28 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_auto_20200215_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_name', models.CharField(max_length=50, verbose_name='收费标准名')),
                ('pay_level_1', models.IntegerField(verbose_name='第一时段')),
                ('pay_level_2', models.IntegerField(verbose_name='第二时段')),
                ('pay_level_3', models.IntegerField(verbose_name='第三时段')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '收费标准',
                'verbose_name_plural': '收费标准',
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_name', models.CharField(max_length=50, verbose_name='活动名')),
                ('discount', models.IntegerField(verbose_name='折扣')),
                ('start_time', models.DateTimeField(blank=True, null=True, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('status', models.CharField(choices=[('1', '正在使用'), ('0', '未使用')], default='0', max_length=2, verbose_name='此收费标准使用状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '折扣',
                'verbose_name_plural': '折扣',
            },
        ),
    ]
