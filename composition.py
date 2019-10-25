#Composition: Two objects are strongly linked, Object A can be thought of as belonging exclusively to Object B. when Object B destroyed, Object A cannot survive UML black diamond
    
#Aggregation: Two objects are weakly linked, neither object has exclusive ownership of the other. UML white diamond

class Student:
    def __init__(self, name, student_number):
        self.name = name
        self.student_number = student_number
        self.classes = []

    def enrol(self, course_running):
        self.classes.append(course_running)
        course_running.add_student(self)


class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, description, course_code, credits):
        self.courses[course_code] = Course(self, description, course_code, credits)
        return self.courses[course_code]


class Course:
    def __init__(self, description, course_code, credits, department):
        self.description = description
        self.course_code = course_code
        self.credits = credits
        self.department = department
        #self.department.add_course(self)

        self.runnings = []

    def add_running(self, year):
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]


class CourseRunning:
    def __init__(self, course, year):
        self.course = course
        self.year = year
        self.students = []

    def add_student(self, student):
        self.students.append(student)


cs_dept = Department("Computer Science", "CS")
cs1010 = cs_dept.add_course("Fundamental of programming 1010", "CS1010", 1)
cs1010_2019 = cs1010.add_running(2019)

bob = Student("Bob", "Smith")
bob.enrol(cs1010_2019)

#relationship
#student can enroll several courese, a course can have multiple students in a time. However, student can exist independently of a course or vice versa
#department offer multiple course, but couse won't exist without department
