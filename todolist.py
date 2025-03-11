from modules.task import Task
from modules.tasklist import TaskList
from modules.terminal import Terminal
from modules.prompt import Prompt
import time
from rich.console import Console

term = Terminal()
console = Console()

myTaskList = TaskList("My Tasks")
myTaskList.build_initial_tasks()


def clear_terminal(func):
    def wrapper():
        term.clear()
        func()  # Don't forget to call the original function you silly

    return wrapper


@clear_terminal
def list_tasks():
    df = myTaskList.get_dataframe_tasks(sendback=True)
    print(df)


@clear_terminal
def list_active_tasks():
    term.clear()
    df = myTaskList.get_dataframe_tasks(sendback=True)
    # print(df)
    print(df.loc[df["status"] != "done"])
    # future improvement - could pass a query to the get_dataframe_tasks function


@clear_terminal
def add_task():
    term.print("What is the name of your task?\n\n", 0.01)
    name = input()
    term.clear()
    term.print("What is the status of your task?\n\n", 0.01)
    status = input()
    term.clear()
    term.print("What is the priority of your task?\n\n", 0.01)
    priority = int(input())
    new_task = Task(name)
    new_task.add_priority(priority)
    new_task.add_status(status)
    myTaskList.add_to_task_list(new_task)
    myTaskList.get_tasks()
    time.sleep(2)
    myTaskList.save_tasks()


def change_task():
    myTaskList.get_dataframe_tasks()
    x = input("What task would you like to change?")
    task = myTaskList.select_task_from_list(x)
    print(task)
    # term.clear()
    term.print(f"{task.name}\n\n", 0.01)
    term.print("What is the status of your task?\n\n", 0.01)
    status = input()
    term.clear()
    term.print("What is the priority of your task?\n\n", 0.01)
    priority = int(input())
    task.add_status(status)
    task.add_priority(priority)
    myTaskList.get_dataframe_tasks()
    time.sleep(2)


def delete_task():
    df = myTaskList.get_dataframe_tasks(sendback=True)
    term.clear()
    term.print(df)
    term.print("\nWhat task would you like to delete?\n\n", 0.01)
    selected_task = input()
    myTaskList.select_task_from_list(selected_task)
    term.clear()
    myTaskList.get_dataframe_tasks()
    time.sleep(2)
    myTaskList.save_tasks()


def exit_program():
    time.sleep(2)
    term.clear()
    term.print("You have exited! DIE 🔪👋\n\n", 0.01)
    time.sleep(1)
    term.clear()
    exit()


time.sleep(1)

main_prompt = Prompt(
    {
        "List Tasks": list_tasks,
        "List Active Tasks": list_active_tasks,
        "Add a Task": add_task,
        "Change a Task": change_task,
        "Delete a Task": delete_task,
    }
)

change_prompt = Prompt({"Task Name": 1, "Task Status": 2, "Task Priority": 3})

try:
    term.clear()
    while 1 == 1:
        try:
            term.print("\nWhat would you like to do?\n\n", 0.01)
            term.ask(main_prompt)
        except ValueError as e:
            term.clear()
            console.print(e, style="white on blue")
            time.sleep(1)
except KeyboardInterrupt:
    exit_program()
