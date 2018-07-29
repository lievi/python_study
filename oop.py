class Employee(object):
    # Class variable
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(self.first, self.last)

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Doe', 70000)

print(Employee.num_of_emps)
