from distutils.command.config import config
from re import L
from django.shortcuts import render
from constance import config

from .models import Projects, Message

def index(request):
    if request.method == 'POST':
        form = request.POST
        email = form.get('email', '')
        name = form.get('name', '')
        text = form.get('message', '')
        if email != '' and name != '' and text != '':
            message = Message.objects.create(
                email=email,
                name=name,
                text=text
            )
            message.save()
    context = {
        'info': config,
        'projects': Projects.objects.all().order_by('pk')
    }
    return render(request, 'Main/index.html', context)