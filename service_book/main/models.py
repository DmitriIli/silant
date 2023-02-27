from django.db import models
from datetime import date

# Create your models here.


def getOperatingTime():
    ...


class Parts(models.Model):
    name = models.CharField(
        primary_key=True, max_length=2, blank=False, unique=True)
    description = models.CharField(default='описание')


class RepairMetod(models.Model):
    name = models.CharField(primary_key=True, max_length=256,
                            blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class ServiceCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class ClientCompany(models.Model):
    name = models.CharField(
        primary_key=True, blank=False, null=False, unique=True)
    description = models.CharField(default='описание')


class Catalog(models.Model):

    # THECHNIC_MODEL = 'THM'
    # ENGINE_MODEL = 'EM'
    # TRANSMSSION_MODEL = 'TRM'
    # DRIVE_AXEL_MODEL = 'DAM'
    # STERING_AXEL_MODEL = 'SAM'
    # SERVICE_COMPANY = 'SC'
    # CLIENT_COMPANY = 'CC'
    # TYPE_OF_MAINTANANCE = 'TM'
    # FAILURE_TYPE = 'FT'
    # REPAIR_METOD = 'RM'

    # catalog = [
    #     THECHNIC_MODEL= 'THM'
    #     ENGINE_MODEL = 'EM'
    #     TRANSMSSION_MODEL = 'TRM'
    #     DRIVE_AXEL_MODEL = 'DAM'
    #     STERING_AXEL_MODEL = 'SAM'
    #     SERVICE_COMPANY = 'SC'
    #     CLIENT_COMPANY = 'CC'
    #     TYPE_OF_MAINTANANCE = 'TM'
    #     FAILURE_TYPE = 'FT'
    #     REPAIR_METOD = 'RM'
    # ]

    CATALOG = [
        ('THM', 'Model of technic'),
        ('EM', 'Engine model'),
        ('TRM', 'Transmission model'),
        ('DAM', 'Drive Axel model'),
        ('SAM', 'Stering Axel model'),
        ('SC', 'Service Company'),
        ('CC', 'Client Company'),
        ('TM', 'Type of Maintanance'),
        ('FT', 'Failure Type'),
        ('RM', 'Repaire Metod')

    ]

    subject = models.CharField(
        max_length=3, choices=CATALOG, blank=False, null=False)
    name = models.CharField(
        primary_key=True, unique=True, blank=False, null=False)
    description = models.CharField(default='описание', blank=False, null=False)


class Machines(models.Model):
    machineFuctoryNumber = models.CharField(
        unique=True, blank=False, null=False)
    machineModel = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    engineFactoryNumber = models.CharField(
        unique=True, blank=False, null=False)
    engineModel = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    transmissionFactoryNumber = models.CharField(
        unique=True, blank=False, null=False)
    transmissionModel = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    driveAxelFactoryNumber = models.CharField(
        unique=True, blank=False, null=False)
    driveAxelModel = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    steringAxelFactoryNumber = models.CharField(
        unique=True, blank=False, null=False)
    steringAxelModel = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    supplyContract = models.CharField(
        unique=True, blank=False, null=False)
    shippingDate = models.DateField(
        default=date.today())
    destination = models.CharField(blank=False, null=False)
    options = models.CharField(
        default='доп. опции отсутствуют')
    clientCompany = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    serviceCompany = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    operatingTime = models.IntegerField(default=0)


class Maintenance(models.Model):
    typeOfMaintance = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    dateOfMaintenance = models.DateField(
        default=date.today(), blank=True, null=True)
    operatingTime = models.IntegerField()
    numberOfOrder = models.CharField(blank=False, null=False)
    dateOfOrder = models.DateField(default=date.today(), blank=True, null=True)
    serviceCompany = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)
    machine = models.ForeignKey(
        Catalog, to_field='name', on_delete=models.DO_NOTHING)


class Complaint(models.Model):

    subject = models.ForeignKey(
        Machines, to_field='name', blank=False, null=False, on_delete=models.DO_NOTHING)
    serviceCompany = models.ForeignKey(
        ServiceCompany, to_field='name', blank=False, null=False, on_delete=models.DO_NOTHING)
    dateOfComplaint = models.DateField(default=date.today())
    operatingTime = models.IntegerField(default=0)
    failureNode = models.ForeignKey(
        Parts, to_field='name', blank=False, null=False)
    description = models.CharField(default='описание', max_length=256)
    repairMetod = models.ForeignKey(
        RepairMetod, to_field='name', blank=False, null=False)
    repairDetails = models.CharField(
        default='используемые части', max_length=256)
    dateComplite = models.DateField(default=date.today())
    downTime = models.IntegerField(default=0)
