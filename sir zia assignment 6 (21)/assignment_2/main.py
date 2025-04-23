class Counter:
    # Class variable to keep track of the count
    count = 0

    def __init__(self):
        # Increment the count whenever a new object is created
        Counter.count += 1

    @classmethod
    def get_count(cls):
        # Class method to return the current count
        return cls.count

# Example usage
if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    print("Number of objects created:", Counter.get_count())