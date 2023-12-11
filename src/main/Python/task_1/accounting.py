from employee import Employee


class Accounting:
    employee: Employee

    def __init__(self, employee):
        self.employee = employee

    def calculate_net_salary(self):
        tax = int(self.employee.base_salary * 0.25)  # рассчитать налог другим способом
        return self.employee.base_salary - tax
