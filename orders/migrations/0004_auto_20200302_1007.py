# Generated by Django 3.0.3 on 2020-03-02 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0007_delete_permissions'),
        ('orders', '0003_remove_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='creator',
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='owners.Owner'),
            preserve_default=False,
        ),
    ]