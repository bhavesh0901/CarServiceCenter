# Generated by Django 3.0.5 on 2021-03-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0016_auto_20210306_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_cart',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]