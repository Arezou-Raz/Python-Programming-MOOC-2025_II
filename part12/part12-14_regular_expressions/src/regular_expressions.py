import re

def is_dotw(my_string: str):
    weeks = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"
    return bool(re.search(weeks, my_string))

def all_vowels(my_string: str):
    pattern = r"^[aeiou]+$"
    return bool(re.search(pattern, my_string))

def time_of_day(my_string: str):
    time = r"^([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
    return bool(re.search(time, my_string))

if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))

    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))

    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
