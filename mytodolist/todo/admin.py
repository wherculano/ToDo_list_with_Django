from django.contrib import admin  # noqa
from .models import TodoItem

# Register your models here.
admin.site.register(TodoItem)
