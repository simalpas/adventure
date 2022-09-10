from django.shortcuts import render

from .models import Room, Item, Person


def index(request):
    room = Room.objects.all().filter(name='start')
    context = {'room': room}
    return render(request, 'adventure/index.html', context)