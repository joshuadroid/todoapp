import pytest
from modules.task import Task


def test_task_happy_path():
    task = Task("Test Task")
    task.add_priority(1)
    task.add_status('To do')
    assert task is not None
    assert task.get_status() is not None
    assert task.get_priority() is not None
    assert isinstance(task.get_priority(), int)
    assert isinstance(task.get_status(), str)