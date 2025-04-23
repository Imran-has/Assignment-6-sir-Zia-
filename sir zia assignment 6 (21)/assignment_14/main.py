#14. Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee

# Example usage
emp = Employee("John")
dept = Department("HR", emp)
print(dept.department_name, dept.employee.name)