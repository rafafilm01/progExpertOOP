#exmaple of a class with call attribute / method 

class Employee:
    #class attributes
    average_age = []
    average_salary = []

    @classmethod
    def avarage_age_of_emps (cls):
        ava_age = sum(cls.average_age) / len (cls.average_age)
        formated_avarage =f"{ava_age:.1f}"
        return formated_avarage
    
    @classmethod
    def avarage_salary_of_emps(cls):
        ava_salary =sum(cls.average_salary) / len(cls.average_salary)
        formated_avaerage = f"{ava_salary:.1f}"
        return formated_avaerage

    def __init__(self, name, age, salary) :
        self.name = name
        self.age = age
        self.salary = salary
        Employee.average_age.append(age)
        Employee.average_salary.append(salary)

brian = Employee("brian", 20, 1000)

marge = Employee("marge", 25, 1500)

steve = Employee("steve", 40, 2000)



print(Employee.average_age)
print(Employee.avarage_age_of_emps())
print(Employee.average_salary)
print(f"the average salary of all our employees is {Employee.avarage_salary_of_emps()}")


## textbook solution 
class Employee:
    number_of_employees = 0
    average_age = 0
    average_salary = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

        total_age = Employee.average_age * Employee.number_of_employees
        total_salary = Employee.average_salary * Employee.number_of_employees
        Employee.average_age = (total_age + age) / (Employee.number_of_employees + 1)
        Employee.average_salary = (total_salary + salary) / (Employee.number_of_employees + 1)
        Employee.number_of_employees += 1