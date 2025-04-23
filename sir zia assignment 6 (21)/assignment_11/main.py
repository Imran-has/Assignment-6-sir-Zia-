#11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

# Example usage
Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)  # Output: 2