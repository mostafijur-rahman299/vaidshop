# Generated by Django 3.0.3 on 2020-03-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendences', '0006_auto_20200302_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='date',
            field=models.DateField(),
        ),
    ]