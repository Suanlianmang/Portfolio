from distutils.command.config import config
from django.shortcuts import render
from constance import config

def index(request):
    context = {
        'info': config,
    }
    return render(request, 'Main/index.html', context)