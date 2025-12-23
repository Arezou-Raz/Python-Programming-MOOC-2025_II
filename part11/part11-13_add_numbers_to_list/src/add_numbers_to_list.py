def add_numbers_to_list(numbers: list):
    last_number = numbers[-1]
    if len(numbers) % 5 != 0:
        numbers.append(last_number + 1)
        add_numbers_to_list(numbers)

if __name__ == '__main__':
    numbers = [1,3,4,5,10,11]
    add_numbers_to_list(numbers)
    print(numbers)
