class Person:
    def __init__(self, name, number):
        self.name  = name
        self.number = number

class Student(Person):
    UNDERGRADUATE = 0
    POSTGRADUATE = 1

    def __init__(self, name, number, studentType):
        super().__init__(name, number)
        self.studentType = studentType
        self.gpa = ()
        self.classes = []

    def enrollCourse(self, course):
        self.enrollCourse(course)

    def __str__(self):
        return "\n이름="+self.name+"\n주민번호="+self.number+\
        "\n수강과목="+str(self.classes)+"\n평점="+str(self.gpa)