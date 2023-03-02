from django.shortcuts import render
from .models import Machine

# Create your views here.


def index(request):

    context = {}

    if not request.user.is_authenticated:
        context = Machine.objects.all().values('modelMachine','factoryNumberMachine',
                                               'engine','factoryNumberEngine', 'transmission',
                                               'factoryNumberTransmission', 'driveAxel',
                                               'factoryNumberDriveAxel', 'steringAxel', 'factoryNumberSteringAxel')

    else:
        context = Machine.objects.all().values()
        
    keys = context[0].keys()
        

    for item in context:
        print(item)
        for key in keys:
            print(key)
            print(item.get(key))

    return render(request, 'index.html', {'context': context, 'keys': keys},)
