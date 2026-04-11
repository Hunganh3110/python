from .employee import Employee

class Manager(Employee):
    def __init__(self, emp_id, name, age):
        super().__init__(emp_id, name, age)
        self.salary = 2000

    def get_salary(self):
        return self.salary