from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='main'),
    path('main/', main, name='none'),

]
