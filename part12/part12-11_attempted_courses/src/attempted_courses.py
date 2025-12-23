class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def names_of_students(attempts: list) -> list:
    return list(map(lambda attempt : attempt.student_name, attempts))

def course_names(attempts: list) -> list:
    course_names_list = map(lambda attempt : attempt.course_name, attempts)
    unique_course_names = set(course_names_list)
    sorted_course_names = sorted(unique_course_names)
    return sorted_course_names

if __name__ == '__main__':
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)

    for name in course_names([s1, s2, s3]):
        print(name)
