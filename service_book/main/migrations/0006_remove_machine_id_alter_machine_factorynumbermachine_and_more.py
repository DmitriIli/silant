# Generated by Django 4.1.7 on 2023-03-01 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_machine_shipingdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='id',
        ),
        migrations.AlterField(
            model_name='machine',
            name='factoryNumberMachine',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.machine'),
        ),
    ]
