import pytest
from django.test import Client

from mytodolist.todo.models import TodoItem


@pytest.mark.django_db
def test_status_code(client: Client):
    resp = client.get('/todo/')
    assert resp.status_code == 200


def test_todoitem_instance():
    todo_item = TodoItem()
    assert todo_item is not None


@pytest.mark.django_db
def test_len_items():
    all_items = TodoItem.objects.all()
    assert len(all_items) == 0


@pytest.mark.django_db
def test_add_items():
    item = TodoItem(content='Test Item')
    item.save()
    assert len(TodoItem.objects.all()) == 1


@pytest.mark.django_db
def test_del_items():
    item = TodoItem(content='Test Item 2')
    item.save()
    assert len(TodoItem.objects.all()) == 1
    item.delete()
    assert len(TodoItem.objects.all()) == 0
