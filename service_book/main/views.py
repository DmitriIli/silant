from django.shortcuts import render
from .models import Machine

# Create your views here.


def index(request):
    context = {}
    if not request.user.is_authenticated:
        context = Machine.objects.all().values('modelMachine', 'factoryNumberMachine',
                                               'engine', 'factoryNumberEngene', 'transmission',
                                               'factoryNumberTransmission', 'driveAxel',
                                               'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')
    else:
        print(request.user)

    return render(request, 'default.html', {'context':context},)
