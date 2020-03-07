# Generated by Django 3.0.3 on 2020-03-04 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocktype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='stocktype',
            name='name',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='stocktype',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]