# Generated by Django 3.0.3 on 2020-03-02 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendences', '0004_auto_20200302_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendence',
            name='day',
        ),
        migrations.AddField(
            model_name='attendence',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]