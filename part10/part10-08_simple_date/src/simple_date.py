class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other: "SimpleDate"):
        return (self.day, self.month, self.year) == (other.day, other.month, other.year)

    def __ne__(self, other: "SimpleDate"):
         return not self.__eq__(other)

    def __lt__(self, other: "SimpleDate"):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day

    def __gt__(self, other: "SimpleDate"):
        if self.year != other.year:
            return self.year > other.year
        if self.month != other.month:
            return self.month > other.month
        return self.day > other.day

    def __add__(self, days: int):
        new_day = self.day + days
        new_month = self.month
        new_year = self.year

        while new_day > 30:
            new_day -= 30
            new_month += 1
            if new_month > 12:
                new_month -= 12
                new_year += 1

        return SimpleDate(new_day, new_month, new_year)

    def __sub__(self, other: "SimpleDate"):
        days1 = self.day + self.month * 30 + self.year * 360
        days2 = other.day + other.month * 30 + other.year * 360

        return abs(days1 - days2)

if __name__ == '__main__':
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)

