from django.shortcuts import render  # noqa
from django.http import HttpResponseRedirect  # noqa
from .models import TodoItem


# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',
                  {'all_todo_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo/')
