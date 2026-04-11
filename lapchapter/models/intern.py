from .employee import Employee

class Intern(Employee):
    def __init__(self, emp_id, name, age):
        super().__init__(emp_id, name, age)
        self.salary = 800

    def get_salary(self):
        return self.salary