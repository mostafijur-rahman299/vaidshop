# Generated by Django 3.0.3 on 2020-03-01 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0006_permissions'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Permissions',
        ),
    ]