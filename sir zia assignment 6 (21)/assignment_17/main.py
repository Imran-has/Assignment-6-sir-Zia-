#17. Function to add a greeting method to a class
def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

# Example usage
p = Person()
print(p.greet())