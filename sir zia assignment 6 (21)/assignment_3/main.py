#3. Public Variables and Methods
class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(f"The {self.brand} car is starting.")

# Example usage
car = Car("Toyota")
print(car.brand)  # Accessing public variable
car.start()       # Accessing public method