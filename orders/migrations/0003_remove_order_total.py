# Generated by Django 3.0.3 on 2020-02-23 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderproduct_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]
