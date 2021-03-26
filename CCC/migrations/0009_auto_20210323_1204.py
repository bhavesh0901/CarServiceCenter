# Generated by Django 3.0.5 on 2021-03-23 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCC', '0008_customer_order_parts_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Order Confirmed', 'Order Confirmed'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered')], default='Pending', max_length=50, null=True),
        ),
    ]