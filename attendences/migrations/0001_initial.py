# Generated by Django 3.0.3 on 2020-03-09 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('entry_time', models.TimeField(null=True)),
                ('exit_time', models.TimeField(blank=True, help_text='When you get home from work, fill out this field', null=True)),
                ('is_approved', models.BooleanField(default=True, null=True, verbose_name='approval status')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Employee')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
