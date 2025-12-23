class CourseRecord:
    def __init__(self) -> None:
        self.__courses = {}

    def add_course(self, course: str, grade: int, credit: int):
        if not course in self.__courses:
            self.__courses[course] = {"grade": grade, "credit": credit}
        else:
            data = self.__courses[course]
            if grade > data['grade']:
                self.__courses[course] = {"grade": grade, "credit": credit}

    def get_data(self, course: str):
        if not course in self.__courses:
            return None
        data = self.__courses[course]
        return f"{course} ({data['credit']} cr) grade {data['grade']}"

    def all_data(self):
        return self.__courses

class Application:
    def __init__(self) -> None:
        self.__courses = CourseRecord()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.__courses.add_course(course, grade, credit)

    def search(self):
        course = input("course: ")
        data = self.__courses.get_data(course)
        if data == None:
            print("no entry for this course")
            return
        print(data)

    def statistics(self):
        data = self.__courses.all_data()
        credits = sum(course['credit'] for course in data.values())
        mean = sum(course['grade'] for course in data.values()) / len(data)
        print(f"{len(data)} completed courses, a total of {credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        for i in range(5, 0, -1):
            count = 0
            for course in data.values():
                if course['grade'] == i:
                    count += 1
            print(f"{i}:", "x" * count)

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.search()
            elif command == "3":
                self.statistics()
            else:
                self.help()

Application().execute()
