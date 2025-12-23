class Task:
    next_id = 1

    def __init__(self, description: str, programmer: str, workload: int):
        self.id = Task.next_id
        Task.next_id += 1
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finnished = False

    def is_finished(self):
        return self.finnished

    def mark_finished(self):
        self.finnished = True

    def __str__(self) -> str:
        status = "FINISHED" if self.finnished else "NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {status}"

class OrderBook:
    def __init__(self):
        self.__tasks = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.__tasks.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.__tasks

    def programmers(self):
        return list(set([t.programmer for t in self.__tasks]))

    def mark_finished(self, id: int):
        for task in self.__tasks:
            if task.id == id:
                task.mark_finished()
                return
        raise ValueError(f"No task found with ID {id}")

    def finished_orders(self):
        return [task for task in self.__tasks if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.__tasks if not task.is_finished()]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"No programmer found with name '{programmer}'")

        finished_tasks = [task for task in self.__tasks if task.programmer == programmer and task.is_finished()]
        unfinished_tasks = [task for task in self.__tasks if task.programmer == programmer and not task.is_finished()]

        finished_hours = sum(task.workload for task in finished_tasks)
        unfinished_hours = sum(task.workload for task in unfinished_tasks)

        return len(finished_tasks), len(unfinished_tasks), finished_hours, unfinished_hours

class Application:
    def __init__(self) -> None:
        self.orders = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmers")

    def add_order(self):
        try:
            description = input("description: ")
            prog_load = input("programmer and workload estimate:").split()
            self.orders.add_order(description, prog_load[0], int(prog_load[-1]))
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished(self):
        if not self.orders.finished_orders():
            print("no finished tasks")
        else:
            for task in self.orders.finished_orders():
                print(task)

    def list_unfinished(self):
        if not self.orders.unfinished_orders():
            print("no unfinished tasks")
        else:
            for task in self.orders.unfinished_orders():
                print(task)

    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.orders.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def programmers(self):
        print(self.orders.programmers() if self.orders.programmers() else None)

    def status(self):
        programmer = input("programmer: ")
        try:
            info = self.orders.status_of_programmer(programmer)
            print(f"tasks: finished {info[0]} not finished {info[1]}, hours: done {info[2]} scheduled {info[3]}")
        except ValueError:
            print("erroneous input")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished()
            elif command == "3":
                self.list_unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status()
            else:
                self.help()

Application().execute()
