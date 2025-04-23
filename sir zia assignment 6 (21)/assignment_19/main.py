#19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value

# Example usage
multiplier = Multiplier(5)
print(callable(multiplier))  # Output: True
print(multiplier(10))        # Output: 50