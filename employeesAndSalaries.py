class Employee:
    def __init__(self, fname, lname, salary):
        self.firstName = fname
        self.lastName = lname
        self.salary = salary

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current employees:')
        for i in self.employees:
            print (i.firstName, i.lastName)
            print ('----------')
    def distribute_paycheck(self):
        for employee in self.employees:
            print ('Paycheck for', employee.firstName, employee.lastName, 'is:')
            print (f' Amount :  ${(employee.salary)/12/2:,.2f}')        


def main():
    my_company = Company()

    employee1 = Employee('Sarah', 'Hess', 50000)
    my_company.add_employee(employee1)
    employee2 = Employee('Lee', 'Lo', 10000)
    my_company.add_employee(employee2)
    employee3 = Employee('Lev', 'Dzhepko', 80000)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.distribute_paycheck()

main()
