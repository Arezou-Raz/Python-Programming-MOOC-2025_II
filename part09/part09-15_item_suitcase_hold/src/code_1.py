class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcase_items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__suitcase_items.append(item)

    def weight(self):
        return sum(item.weight() for item in self.__suitcase_items)

    def print_items(self):
        for item in self.__suitcase_items:
            print(item)

    def heaviest_item(self):
        if not self.__suitcase_items:
            return None
        return max(self.__suitcase_items, key=lambda item: item.weight())

    def items(self):
        return self.__suitcase_items

    def __str__(self):
        if len(self.__suitcase_items) == 1:
            return f"{len(self.__suitcase_items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__suitcase_items)} items ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__cargo_items = []

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__cargo_items.append(suitcase)

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.__cargo_items)

    def print_items(self):
        for suitcase in self.__cargo_items:
            for item in suitcase.items():
                print(item)

    def __str__(self):
        if len(self.__cargo_items) == 1:
            return f"{len(self.__cargo_items)} suitcase, space for {self.__max_weight - self.weight()} kg"
        else:
            return f"{len(self.__cargo_items)} suitcases, space for {self.__max_weight - self.weight()} kg"

if __name__ == '__main__':
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

