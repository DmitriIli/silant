# Generated by Django 4.1.7 on 2023-03-01 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_servicecompanyuser_manageruser_clientuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='complainte',
            name='maintenanceCompany',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.maintenancecompany'),
            preserve_default=False,
        ),
    ]
