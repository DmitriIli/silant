from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import SignupForm




class BaseRegisterView(CreateView):
    model = User
    form_class = SignupForm
    success_url = '/sign/login/'


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            return render(request, 'sign/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'sign/signup.html', {'form': form})

