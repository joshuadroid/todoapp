from modules.task import Task
from modules.tasklist import TaskList


def test_task_happy_path():
    task = Task("Test Task")
    task.add_priority(1)
    task.add_status("To do")
    assert task is not None
    assert task.get_status() is not None
    assert task.get_priority() is not None
    assert isinstance(task.get_priority(), int)
    assert isinstance(task.get_status(), str)


def test_get_lists():
    myTaskList = TaskList("My Tasks")
    myTaskList.build_initial_tasks()
    assert myTaskList.get_tasks() is not None
    assert myTaskList.get_active_tasks() is not None
    for x in myTaskList.get_active_tasks():
        assert str(x.get_status()).lower() is not "done"
