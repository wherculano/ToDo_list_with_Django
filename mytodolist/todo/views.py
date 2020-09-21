from django.shortcuts import render  # noqa
from django.http import HttpResponse  # noqa


# Create your views here.
def todoView(request):
    return render(request, 'todo.html')
