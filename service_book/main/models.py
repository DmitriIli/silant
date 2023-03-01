from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


def getOperatingTime():
    ...


class ServiceCompanyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(
        'ServiceCompany', to_field='name', on_delete=models.CASCADE)


class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clientCompany = models.ForeignKey(
        'ClientCompany', to_field='name', on_delete=models.CASCADE)


class ManagerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Parts(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)


class ModelMachine(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class Engine(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class Transmission(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class DriveAxel(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class SteringAxel(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class ServiceCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class MaintenanceCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class ClientCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class TypeOfService(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class RecoveryMethod(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True, max_length=64)
    description = models.CharField(default='описание', max_length=256)


class Machine(models.Model):
    modelMachine = models.ForeignKey(
        ModelMachine, to_field='name', on_delete=models.CASCADE)
    factoryNumberMachine = models.CharField(
        primary_key=True, max_length=64, unique=True)
    engine = models.ForeignKey(
        Engine, to_field='name', on_delete=models.CASCADE)
    factoryNumberEngene = models.CharField(max_length=64, unique=True)
    transmission = models.ForeignKey(
        Transmission, to_field='name', on_delete=models.CASCADE)
    factoryNumberTransmission = models.CharField(max_length=64, unique=True)
    driveAxel = models.ForeignKey(
        DriveAxel, to_field='name', on_delete=models.CASCADE)
    factoryNumberDriveAxel = models.CharField(max_length=64, unique=True)
    steringAxel = models.ForeignKey(
        SteringAxel, to_field='name', on_delete=models.CASCADE)
    factoryNumberSteringAxel = models.CharField(max_length=64, unique=True)
    supplyContract = models.CharField(max_length=64)
    shipingDate = models.DateField(default=date.today())
    receiver = models.CharField(max_length=64)
    deliveryAddress = models.CharField(max_length=256)
    equipment = models.CharField(
        max_length=256,  default='стандартная комплектация')
    client = models.ForeignKey(
        ClientCompany, to_field='name', on_delete=models.CASCADE)
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE)


class Service(models.Model):
    typeOfService = models.ForeignKey(
        TypeOfService, to_field='name', on_delete=models.CASCADE)
    dateService = models.DateField(auto_now_add=True)
    operatingTime = models.IntegerField(default=0)
    orderNumber = models.CharField(max_length=64)
    orderDate = models.DateField(auto_now_add=True)
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE)
    machine = models.ForeignKey(
        Machine, to_field='factoryNumberMachine', on_delete=models.CASCADE)


class Complainte(models.Model):
    machine = models.ForeignKey(
        Machine, to_field='factoryNumberMachine', on_delete=models.CASCADE)
    failureDate = models.DateField(auto_now_add=True)
    operatingTime = models.IntegerField(default=0)
    failurePart = models.ForeignKey(
        Parts, to_field='name', on_delete=models.CASCADE)
    failureDescription = models.CharField(max_length=256, default='описание')
    recoveryMethod = models.ForeignKey(
        RecoveryMethod, to_field='name', on_delete=models.CASCADE)
    spareParts = models.CharField(default='зап.части', max_length=256)
    recoveryDate = models.DateField(auto_now_add=True)
    downTime = models.IntegerField(default=0)
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', on_delete=models.CASCADE)
    maintenanceCompany = models.ForeignKey(
        MaintenanceCompany, to_field='name', on_delete=models.CASCADE)
