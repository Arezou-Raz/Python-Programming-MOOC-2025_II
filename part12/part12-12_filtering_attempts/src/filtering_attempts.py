class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list) -> list:
    return filter(lambda attempt : attempt.grade > 0, attempts)

def attempts_with_grade(attempts: list, grade: int) -> list:
    return filter(lambda attempt : attempt.grade == grade, attempts)

def passed_students(attempts: list, course: str) -> list:
    wanted_course = filter(lambda attempt : attempt.course_name == course, attempts)
    passed_wanted_course = filter(lambda passed : passed.grade > 0, wanted_course)
    passed_wanted_course_names = map(lambda name : name.student_name, passed_wanted_course)
    sorted_passed_wanted_course_names = sorted(passed_wanted_course_names)
    return sorted_passed_wanted_course_names

if __name__ == '__main__':
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
