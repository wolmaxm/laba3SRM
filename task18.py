class Employee: 
    def __init__(self, name='John Doe', age='', position='', pay=''):
        self.name = name
        self.age = age
        self.position = position
        self.pay = pay
        print('Створено користувача для нового співробітника:' + name)
        
    def printDetails(self):
        print("Ім'я", self.name)
        print("Вік" , self.age)
        print("Посада", self.position)
        print("Зарплата", self.pay)
        
    def enroll(self, newpay):
        self.pay += newpay
        
    def promote(self, new_position):
        old_position = self.position
        self.position = new_position
        
employee1= Employee("Орос Максим", 42, "Студент", 2000)
 
employee1.printDetails()

employee1.promote('Сенйор')
employee1.enroll(50000)

employee1.printDetails()
        