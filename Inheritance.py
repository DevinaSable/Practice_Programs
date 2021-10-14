class Person():
    def __init__(self, name):                  #Constructor
         self.name = name

    def getName(self):                      #to get name
        return self.name

    def isEmployee(self):               # to check if this person is employee
        return False

class Employee(Person):              #Inherited or sub class( Note Person is in bracket)
    def isEmployee(self):              # Here we return True
        return True

emp = Person("Geek1")                  #Driver code | An object of Person
print(emp.getName(), emp.isEmployee())
emp = Employee("Geek2")                  #An object of Employee
print(emp.getName(), emp.isEmployee())