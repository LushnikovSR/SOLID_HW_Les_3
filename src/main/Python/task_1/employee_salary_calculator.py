class EmployeeSalaryCalculator:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_net_salary(self):
        tax = int(self.employee.base_salary * 0.25)
        return self.employee.base_salary - tax
