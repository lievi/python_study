from typing import List


class Employee():

    raise_amt = 1.04

    def __init__(self, first: str, last: str, pay: int):
        """Função construtora da classe de emprego.

        Arguments:
            first {str} -- primeiro nome
            last {str} -- Ultimo nome
            pay {int} -- Valor pago
        """
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first.lower(), self.last.lower())

    @property
    def fullname(self) -> str:
        """Retorna o Nome e Sobrenome do empregado.
        """
        return "{} {}".format(self.first.capitalize(), self.last.capitalize())

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name")
        self.first = None
        self.last = None

    def apply_raise(self):
        """Aplica aumento no salário do empregado.
        """
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last,
                                                   self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self,
                 first: str,
                 last: str,
                 pay: int,
                 employees: List[Employee] = None):

        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_emp(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev_1 = Developer("lievi", "silva", 50000, "python")
dev_2 = Developer("John", "DOE", 30000, 'C#')

mng_1 = Manager("Sue", "smith", 90000, [dev_1])

print(dev_1.first)
dev_1.fullname = "Vida Loka"
print(dev_1.email)
del dev_1.fullname
