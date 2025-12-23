def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1

    for number in range(beginning, maximum + 1, 2):
        yield number

if __name__ == '__main__':
    numbers = even_numbers(2, 10)
    for number in numbers:
        print(number)

    numbers1 = even_numbers(11, 21)
    for number in numbers1:
        print(number)

