# Generated by Django 2.0.8 on 2020-02-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_time',
            field=models.DateField(blank=True, null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_time',
            field=models.DateField(blank=True, null=True, verbose_name='更新时间'),
        ),
    ]
