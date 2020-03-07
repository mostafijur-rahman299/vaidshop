# Generated by Django 3.0.3 on 2020-02-27 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('owners', '0002_permissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissions',
            name='Book',
        ),
        migrations.RemoveField(
            model_name='permissions',
            name='group',
        ),
        migrations.AddField(
            model_name='permissions',
            name='permission',
            field=models.ManyToManyField(to='auth.Permission'),
        ),
    ]