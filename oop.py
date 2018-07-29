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


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('John', 'Doe', 60000)

import datetime
my_date = datetime.date(2006, 7, 10)
print(Employee.is_workday(my_date))
