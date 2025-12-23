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
        self.orders = []
        self.programmer_set = set()

    def add_order(self, description: str, programmer: str, workload: int):
        task = Task(description, programmer, workload)
        task.id = len(self.orders) + 1
        self.orders.append(task)
        self.programmer_set.add(programmer)

    def mark_finished(self, task_id: int):
        for task in self.orders:
            if task.id == task_id:
                task.mark_finished()
                return
        raise ValueError(f"No task found with ID {task_id}")

    def finished_orders(self):
        return [task for task in self.orders if task.is_finished()]

    def unfinished_orders(self):
        return [task for task in self.orders if not task.is_finished()]

    def all_orders(self):
        return self.orders

    def programmers(self):
        return list(self.programmer_set)

    def status_of_programmer(self, programmer: str):
        finished_count = 0
        unfinished_count = 0
        finished_workload = 0
        unfinished_workload = 0

        for task in self.orders:
            if task.programmer == programmer:
                if task.is_finished():
                    finished_count += 1
                    finished_workload += task.workload
                else:
                    unfinished_count += 1
                    unfinished_workload += task.workload

        if finished_count + unfinished_count == 0:
            raise ValueError(f"No programmer found with name '{programmer}'")

        return finished_count, unfinished_count, finished_workload, unfinished_workload

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)

    status = orders.status_of_programmer("Adele")
    print(status)
