class Student:
    def __init__(self, name="John Doe", courses=[], phone_number="", email_address="",):
        self.name = name
        self.courses = courses
        self.phone_number = phone_number
        self.email_address = email_address
        print("Створено користувача для: " + name)

    def printDetails(self):
        print("Ім'я ", self.name)
        print("Зареєстровані курси ", self.courses)
        print("Номер телефону: ", self.phone_number)
        print("Електрона пошта: ", self.email_address)

    def enroll(self, course):
        self.courses.append(course)

student1 = Student("Mary", ["L548"], "+380631485365", "mary@kpi.ua",)

print("Введіть нові курси для користувача", student1.name)
newcourse = input("Введіть номер курсу або 'stop' ")

while newcourse != "stop":
    student1.enroll(newcourse)
    print("Введіть нові курси для користувача", student1.name)
    newcourse = input("Введіть новий курс або 'stop' ")

student1.printDetails()