class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons_list = []

    def add(self, person: Person):
        self.persons_list.append(person)

    def is_empty(self):
        return len(self.persons_list) == 0

    def total_height(self):
        height_sum = 0
        for person in self.persons_list:
            height_sum += person.height

        return height_sum

    def shortest(self):
        if self.is_empty():
            return None

        shortest_person = self.persons_list[0]
        for person in self.persons_list:
            if person.height < shortest_person.height:
                shortest_person = person

        return shortest_person

    def remove_shortest(self):
        if self.is_empty():
            return None

        shortest_person = self.shortest()
        self.persons_list.remove(shortest_person)

        return shortest_person

    def print_contents(self):
        print(f"There are {len(self.persons_list)} persons in the room, and their combined height is {self.total_height()} cm")
        for person in self.persons_list:
            print(f"{person.name} ({person.height} cm)")

if __name__ == '__main__':
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
