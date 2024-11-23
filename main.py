class Calculator:
    """A simple calculator class."""

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference between two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """Returns the division of two numbers. Raises ValueError for division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
