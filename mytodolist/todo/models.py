from django.db import models  # noqa


# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
