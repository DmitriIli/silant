# Generated by Django 4.1.7 on 2023-03-02 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_modelmachine_options_alter_parts_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='modelMachine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelmachine', verbose_name='Model Machine'),
        ),
    ]