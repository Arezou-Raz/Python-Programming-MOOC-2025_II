class LotteryNumbers:
    def __init__(self, week: int, numbers: list):
        self.week = week
        self.numbers = numbers

    def number_of_hits(self, numbers: list):
        return sum([1 for number in numbers if number in self.numbers])

    def hits_in_place(self, numbers: list):
        return [number if number in self.numbers else -1 for number in numbers]

if __name__ == '__main__':
    week8 = LotteryNumbers(8, [1,2,3,10,20,30,33])
    my_numbers = [1,4,7,10,11,20,30]

    print(week8.hits_in_place(my_numbers))
