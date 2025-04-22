def validate_priority(priority):
    # TODO
    print("TODO")


def validate_status(status):
    if str(status).lower() in ("to do", "in progress", "done"):
        return True
    else:
        return False


class Task:

    def __init__(self, name):
        self.name = name
        self.__status = ""
        self.__priority = ""

    def add_status(self, status):
        self.__status = status
        return self.__status

    def add_priority(self, priority):
        self.__priority = priority
        return self.__priority

    def get_name(self):
        return self.name

    def get_status(self):
        # print(self.__status)
        return self.__status

    def get_priority(self):
        # print(self.__priority)
        return self.__priority

    # def change_priority(self, priority):
    #     if validate_priority(priority) == True:
    #         self.__priority = str(priority).lower()
    #     print(f"{self.name}'s priority changed to {self.__priority}")

    def mark_as_done(self):
        self.__status = "Done"
        print(f"{self.name} marked as done")
