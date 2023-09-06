class Person:
    no_of_persons_in_school = 0

    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.password = password
        Person.no_of_persons_in_school += 1

    def change_password(self):
        current_password = int(input("Enter your current password: "))
        if current_password == self.password:
            new_password = int(input("Enter your new password: "))
            self.password = new_password
            print("Password changed successfully!")
        else:
            print("Incorrect password. Please try again.")

    def describe(self):
        return f"Your name is {self.name} and your age is {self.age}"


class Teacher(Person):
    def __init__(self, name, age, password, salary, working_hours):
        super().__init__(name, age, password)
        self.salary = salary
        self.working_hours = working_hours

    def describe_teacher(self):
        description = super().describe()
        return f"{description} and your salary is {self.salary} and your working hours are {self.working_hours}"

    def get_salary(self):
        current_password = int(input("Enter your current password: "))
        if current_password == self.password:
            print(self.salary)
        else:
            print("Incorrect password. Please try again.")

    def get_working_hours(self):
        current_password = int(input("Enter your current password: "))
        if current_password == self.password:
            print(self.working_hours)
        else:
            print("Incorrect password. Please try again.")


class Student(Person):
    def __init__(self, name, age, password, grades, attendance, courses):
        super().__init__(name, age, password)
        self.grades = grades
        self.attendance = attendance
        self.courses = courses

    def describe_student(self):
        description = super().describe()
        return f"{description} and your grades are {self.grades} and your attendance is {self.attendance} and your courses are {self.courses}"

    def get_grades(self):
        current_password = int(input("Enter your current password: "))
        if current_password == self.password:
            print(self.grades)
        else:
            print("Incorrect password. Please try again.")

    def get_attendance(self):
        current_password = int(input("Enter your current password: "))
        if current_password == self.password:
            print(self.attendance)
        else:
            print("Incorrect password. Please try again.")

    def get_courses(self):
        current_password = int(input("Enter your current password: "))
        if current_password == self.password:
            print(self.courses)
        else:
            print("Incorrect password. Please try again.")


student1 = Student("Ahmed", 15, 123, ["Math=10/20", "Science=19/20", "English=20/20"], "Absent in 20 days this year", ["Math", "Science", "English"])
print(student1.describe_student())

teacher1 = Teacher("Mr. Ali", 42, 12345, 4000, 9)
print(teacher1.describe_teacher())

print(Person.no_of_persons_in_school)