#7. Access Modifiers: Public, Private, and Protected
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

# Example usage
emp = Employee("John", 50000, "123-45-6789")
print(emp.name)          # Accessible
print(emp._salary)       # Accessible but not recommended
# print(emp.__ssn)       # Raises AttributeError
print(emp._Employee__ssn)  # Access private variable using name mangling