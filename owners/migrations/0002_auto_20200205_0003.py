# Generated by Django 3.0.2 on 2020-02-04 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]