# Generated by Django 4.1.7 on 2023-02-28 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCompany',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='DriveAxel',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ModelMachine',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryMethode',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SteringAxel',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfService',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(default='описание', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateService', models.DateField(auto_now_add=True)),
                ('operatingTime', models.IntegerField(default=0)),
                ('orderNumber', models.CharField(max_length=64)),
                ('orderDate', models.DateField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelmachine')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicecompany')),
                ('typeOfService', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.typeofservice')),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factoryNumberMachine', models.CharField(max_length=64, unique=True)),
                ('factoryNumberEngene', models.CharField(max_length=64, unique=True)),
                ('factoryNumberTransmission', models.CharField(max_length=64, unique=True)),
                ('factoryNumberDriveAxel', models.CharField(max_length=64, unique=True)),
                ('factoryNumberSteringAxel', models.CharField(max_length=64, unique=True)),
                ('supplyContract', models.CharField(max_length=64)),
                ('shipingDate', models.DateField(auto_now_add=True)),
                ('receiver', models.CharField(max_length=64)),
                ('deliveryAddress', models.CharField(max_length=256)),
                ('equipment', models.CharField(default='стандартная комплектация', max_length=256)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clientcompany')),
                ('driveAxel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.driveaxel')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.engine')),
                ('modelMachine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelmachine')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicecompany')),
                ('steringAxel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.steringaxel')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.transmission')),
            ],
        ),
        migrations.CreateModel(
            name='Complainte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('failureDate', models.DateField(auto_now_add=True)),
                ('operatingTime', models.IntegerField(default=0)),
                ('failureDescription', models.CharField(default='описание', max_length=256)),
                ('spareParts', models.CharField(default='зап.части', max_length=256)),
                ('recoveryDate', models.DateField(auto_now_add=True)),
                ('downTime', models.IntegerField(default=0)),
                ('failurePart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.parts')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.modelmachine')),
                ('recoveryMethod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.recoverymethode')),
                ('serviceCompany', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.servicecompany')),
            ],
        ),
    ]
