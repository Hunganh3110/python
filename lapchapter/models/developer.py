from .employee import Employee

class Developer(Employee):
    def __init__(self, emp_id, name, age, language):
        super().__init__(emp_id, name, age)
        self.language = language
        self.salary = 1500

    def get_salary(self):
        return self.salary