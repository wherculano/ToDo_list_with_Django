from django.shortcuts import render  # noqa
from django.http import HttpResponse


# Create your views here.
def todoView(request):
    return HttpResponse('This is my ToDoView')
