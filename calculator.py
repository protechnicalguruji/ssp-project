class Calculator:
    def add(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Inputs must be numbers (int or float)")
        return x + y

    def subtract(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Inputs must be numbers (int or float)")
        return x - y

    def multiply(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Inputs must be numbers (int or float)")
        return x * y

    def divide(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Inputs must be numbers (int or float)")
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
