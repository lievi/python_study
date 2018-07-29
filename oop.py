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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Contrutor alternativo que recebe os parâmetros como string.

        Arguments:
            emp_str {str} -- A string com os parâmetros separados por hifén

        Returns:
            Employee -- Nova instância da classe employee

        """
        first, last, pay = emp_str.split('-')
        # Retornando uma nova instância da classe (cls, tipo um self)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        """
        Exemplo de função estática.

        A função estática é uma função que não precisa do self ou cls
        É somente algum pedaço de lógica que faz sentido para a classe.

        Arguments:
            day {datetime} -- O dia para ser verificado

        Returns:
            Boolean -- Se é workday ou não

        """
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        # O super() meio que chama a função do pai
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    raise_amount = 1.10


emp_1 = Developer('Corey', 'Schafer', 50000, 'Python')
emp_2 = Developer('John', 'Doe', 60000, 'C#')

mgr_1 = Manager('Sue', 'Smith', 90000, [emp_1])

print(issubclass(Developer, Manager))
