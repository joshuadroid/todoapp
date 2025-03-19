from modules.task import Task
from modules.tasklist import TaskList
from modules.terminal import Terminal
from modules.prompt import Prompt
import time
from rich.console import Console
from flask import Flask, redirect, url_for, request
import json

term = Terminal()
console = Console()

myTaskList = TaskList("My Tasks")
myTaskList.build_initial_tasks()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def clear_terminal(func):
    def wrapper():
        term.clear()
        func()  # Don't forget to call the original function you silly

    return wrapper


# TODO Add sanitize for input
# def sanitize_input(func):
#     def wrapper():
#         make sure priority is int
#         make sure status is in ("to do" "in progress" or "done")
#         return func
#     someReturnVal = wrapper()
#     return someReturnVal


# @clear_terminal
@app.route("/tasks/")
def list_tasks():
    print("Listed Tasks!")
    return json.dumps(myTaskList.get_tasks())


# @clear_terminal
@app.route("/active_tasks")
def list_active_tasks():
    print("Listed Active Tasks!")
    return json.dumps(myTaskList.get_active_tasks())


# @clear_terminal
# @sanitize_input
@app.route("/addtask", methods=['POST', 'GET'])
def add_task():
    print(request.method)
    print(request.args)
    print(request.form)
    name = request.form['newtask']
    status = request.form['newstatus']
    priority = int(request.form['newpriority'])
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


# @clear_terminal
def delete_task():
    df = myTaskList.get_dataframe_tasks(sendback=True)
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

main_prompt = Prompt(
    {
        "List Tasks": list_tasks,
        "List Active Tasks": list_active_tasks,
        "Add a Task": add_task,
        "Change a Task": change_task,
        "Delete a Task": delete_task,
    }
)

if __name__ == '__main__':
    app.run(debug=True)

# change_prompt = Prompt({"Task Name": 1, "Task Status": 2, "Task Priority": 3})

# try:
#     term.clear()
#     while 1 == 1:
#         try:
#             term.print("\nWhat would you like to do?\n\n", 0.01)
#             term.ask(main_prompt)
#         except ValueError as e:
#             term.clear()
#             console.print(e, style="white on blue")
#             time.sleep(1)
# except KeyboardInterrupt:
#     exit_program()
