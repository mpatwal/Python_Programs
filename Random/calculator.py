class BasicCalculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Division by zero Not Possible ! :( "
        return a / b


calc = BasicCalculator()
print("Addition: 4 + 6 =", calc.add(4, 6))
print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
print("Multiplication: 12 * 3 =", calc.multiply(12, 3))
print("Division: 5 / 0 =", calc.divide(5, 0))
print("Division: 5 / 2 =", calc.divide(5, 2))
