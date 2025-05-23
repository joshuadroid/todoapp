import pandas as pd
from modules.task import Task
from rich.console import Console
import sqlite3
import json

console = Console(style="blue bold")


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Task):
            return {"priority": obj.get_priority(), "name": obj.name, "is_done": obj.get_status()}
        return json.JSONEncoder.default(self, obj)


def validate_status(status):
    if str(status).lower() in ("to do", "in progress", "done"):
        return True
    else:
        return False


columns = ["name", "status", "priority"]
file_path = "tasks.csv"

con = sqlite3.connect("tutorial.db")


class TaskList:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def build_initial_tasks_with_sqlite(self):
        # try to open sqlite
        # except FileNotFound:
        # build out sqlite file for tasks

        # return tasks
        # save file
        return

    def build_initial_tasks(self):
        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            base_tasks = {
                "name": ["Send Alex Arch Manning Memes", "Send Jeff Pics", "Tell Mitch he has great hair"],
                "status": ["to do", "in progress", "done"],
                "priority": [2, 1, 3],
            }
            df = pd.DataFrame(data=base_tasks)
            df.to_csv("tasks.csv", index=False)
        print(df)
        g = 0
        while g < len(df):
            print(df["name"][g])
            print(df["status"][g])
            print(df["priority"][g])
            task = Task(df["name"][g])
            task.add_priority(df["priority"][g])
            task.add_status(df["status"][g])
            self.add_to_task_list(task)
            # task = df['name'][g]
            g += 1
        return df

    def __get_list_of_tasks(self):
        tasks = []
        for x in self.tasks:
            list_data = []
            list_data.append(x.name)
            list_data.append(x.get_status())
            list_data.append(int(x.get_priority()))
            tasks.append(list_data)
            # print(data)
        return tasks

    def get_tasks(self):
        # for x in self.tasks:
        # console.print(f"Task: {x.name} || priority #{x.get_priority()} || status: {x.get_status()}")
        tasks = self.__get_list_of_tasks()
        print(tasks)
        return tasks

    def get_dataframe_tasks(self):
        data = []
        for x in self.tasks:
            list_data = []
            list_data.append(str(x.name))
            list_data.append(str(x.get_status()))
            list_data.append(int(x.get_priority()))
            data.append(list_data)
            # print(data)
        df = pd.DataFrame(data=data, columns=columns).sort_values("priority")
        return df

    def get_active_tasks(self):
        tasks = self.__get_list_of_tasks()
        num = 0
        for x in tasks:
            if str(x[1]).lower() == "done" or "deleted":
                tasks.pop(num)
            num += 1
        return tasks

    def add_to_task_list(self, task):
        self.tasks.append(task)
        return self.tasks

    def select_task_from_list(self, priority):
        priority = int(priority)
        for task in self.tasks:
            print(task.get_priority())
            if priority == task.get_priority():
                return task
        return ValueError

    def delete_task(self, number):
        print(f"The number is: {number}")
        the_list = self.__get_list_of_tasks()
        print(the_list)
        x = 0
        for task in self.tasks:
            print(task)
            print("===========")
            print(f"Testing if {task.get_priority()} == {number}")
            if int(task.get_priority()) == int(number):
                task.add_status("deleted")
                print(f"Status of {task.name} is now {task.get_status()}")
            x += 1
            print(x)

        self.__get_list_of_tasks()

        print(the_list)
        # TODO: look into serializer to print object
        # figure out how to delete object based on priority
        print("૮₍˶Ó﹏Ò ⑅₎ა")
        return self

    def save_tasks(self):
        print("Starting to Save")
        df = self.get_dataframe_tasks()
        df.to_csv(file_path, index=False)
        print("Save Successful!")
