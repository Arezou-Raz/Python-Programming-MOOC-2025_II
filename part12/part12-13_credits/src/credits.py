from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda credits_sum, attempt: credits_sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed_ones = filter(lambda attempt : attempt.grade > 0, attempts)
    return reduce(lambda credits_sum, attempt: credits_sum + attempt.credits, passed_ones, 0)

def average(attempts: list):
    passed_ones = list(filter(lambda attempt : attempt.grade > 0, attempts))
    sum_of_grades = reduce(lambda grade_sum, attempt: grade_sum + attempt.grade, passed_ones, 0)
    count_of_passed_ones = len(passed_ones)

    if count_of_passed_ones == 0:
        return 0

    return sum_of_grades / count_of_passed_ones

if __name__ == '__main__':
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    ag = average([s1, s2, s3])
    print(ag)
