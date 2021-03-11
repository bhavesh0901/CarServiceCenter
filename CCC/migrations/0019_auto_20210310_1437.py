# Generated by Django 3.0.5 on 2021-03-10 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0018_auto_20210308_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parts_subcategory',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order_cart',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_cart',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]