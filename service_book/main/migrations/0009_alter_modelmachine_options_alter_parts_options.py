# Generated by Django 4.1.7 on 2023-03-02 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_factorynumberengene_machine_factorynumberengine_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modelmachine',
            options={'verbose_name': 'Model'},
        ),
        migrations.AlterModelOptions(
            name='parts',
            options={'verbose_name': 'Parts'},
        ),
    ]