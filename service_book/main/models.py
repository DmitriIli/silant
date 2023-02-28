from django.db import models
from datetime import date

# Create your models here.


def getOperatingTime():
    ...


class Parts(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)


class ModelMachine(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class Engine(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class Transmission(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class DriveAxel(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class SteringAxel(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class ServiceCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class ClientCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class TypeOfService(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class RecoveryMethode(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')

# repair methods


class Machine(models.Model):
    modelMachine = models.ForeignKey(ModelMachine, to_field='name')
    factoryNumberMachine = models.CharField(max_length=64, unique=True)
    engine = models.ForeignKey(Engine, to_field='name')
    factoryNumberEngene = models.CharField(max_length=64, unique=True)
    transmission = models.ForeignKey(Transmission, to_field='name')
    factoryNumberTransmission = models.CharField(max_length=64, unique=True)
    driveAxel = models.ForeignKey(DriveAxel, to_field='name')
    factoryNumberDriveAxel = models.CharField(max_length=64, unique=True)
    steringAxel = models.ForeignKey(SteringAxel, to_field='name')
    factoryNumberSteringAxel = models.CharField(max_length=64, unique=True)
    supplyContract = models.CharField(max_length=64)
    shipingDate = models.DateField(default=date.today())
    receiver = models.CharField(max_length=64)
    deliveryAddress = models.CharField(max_length=128)
    equipment = models.CharField(
        max_length=128,  default='стандартная комплектация')
    client = models.ForeignKey(ClientCompany, to_field='name')
    serviceCompany = models.ForeignKey(ServiceCompany, to_field='name')


class Service(models.Model):
    typeOfService = models.ForeignKey(TypeOfService, to_field='name')
    dateService = models.DateField(default=date.today())
    operatingTime = models.IntegerField(default=0)
    order = models.CharField(max_length=64)
    orderDate = models.DateField(default=date.today())
    serviceCompany = models.ForeignKey(ServiceCompany, to_field='name')
    machine = models.ForeignKey(Machine, to_field='name')


class Complainte(models.Model):
    machine = models.ForeignKey(Machine, to_field='name')
    failureDate = models.DateField(default=date.today())
    operatingTime = models.IntegerField(default=0)
    failurePart = models.ForeignKey(Parts, to_field='name')
    failureDescription = models.CharField(max_length=256, default='описание')
    recoveryMethod = models.ForeignKey(RecoveryMethode, to_field='name')
    spareParts = models.CharField(default='зап.части')
    recoveryDate = models.DateField(default=date.today())
    downTime = models.IntegerField(default=0)
    serviceCompany = models.ForeignKey(ServiceCompany, to_field='name')
