# Generated by Django 3.0.3 on 2020-03-02 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
        ('attendences', '0002_auto_20200302_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='employee',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee'),
            preserve_default=False,
        ),
    ]