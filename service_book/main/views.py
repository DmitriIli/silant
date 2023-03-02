from django.shortcuts import render
from .models import Machine

# Create your views here.


def main(request):
    context = {}
    return render(request, 'main.html', {'context': context},)


def index(request):

    context = {}

    if not request.user.is_authenticated:
        context = Machine.objects.all().values('modelMachine', 'factoryNumberMachine',
                                               'engine', 'factoryNumberEngine', 'transmission',
                                               'factoryNumberTransmission', 'driveAxel',
                                               'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')

    else:
        context = Machine.objects.all().values()

        # Model._meta.get_field('<field name>').verbose_name

    keys = context[0].keys()
    ls = [item for item in keys]

    verboseNames = [Machine._meta.get_field(
        f'{name}').verbose_name for name in ls]

    return render(request, 'index.html', {'context': context, 'verboseNames': verboseNames},)
