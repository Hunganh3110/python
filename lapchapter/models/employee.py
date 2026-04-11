class Employee:
    def __init__(self, emp_id, name, age):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.performance = 0
        self.projects = []

    def __str__(self):
        return f"{self.emp_id} - {self.name} - {self.age} tuổi - Điểm: {self.performance} - Projects: {len(self.projects)}"