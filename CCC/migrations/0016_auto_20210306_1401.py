# Generated by Django 3.0.5 on 2021-03-06 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0015_auto_20210305_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_cart',
            name='net_total',
        ),
        migrations.RemoveField(
            model_name='order_cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order_cart',
            name='subtotal',
        ),
        migrations.RemoveField(
            model_name='order_cart',
            name='total',
        ),
    ]
