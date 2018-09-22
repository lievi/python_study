from typing import List


class Employee:

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
        self.email = "{}.{}@email.com".format(
            self.first.lower(), self.last.lower())
        self.pay = pay

    def fullname(self) -> str:
        """Retorna o Nome e Sobrenome do empregado.
        """
        return "{} {}".format(self.first.capitalize(), self.last.capitalize())

    def apply_raise(self):
        """Aplica aumento no salário do empregado.
        """
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first: str, last: str, pay: int, employees: List[Employee] = None):

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

mng_1 = Manager("Sue", "smith", 90000, "nhjas")

print(mng_1.email)
mng_1.add_emp(dev_2)
mng_1.remove_emp(dev_1)
mng_1.print_emps()

# print(dev_1.fullname())
# print(dev_2.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
