class Student:
    def __init__(self, name, marks):
        # Initialize attributes using self
        self.name = name
        self.marks = marks

    def display(self):
        # Display student details
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Alice", 85)
student1.display()