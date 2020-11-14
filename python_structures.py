class MathOperations:

    def add_numbers(self, a, b):
        result = a + b
        return result

    def multiply_numbers(self, a, b):
        result = a * b
        return result

    def divide_numbers(self, a, b):
        result = a / b
        return result

calculator = MathOperations()


def test_positive():
    result = calculator.add_numbers(1, 2)
    assert result == 3


def test_negative():
    result = calculator.add_numbers(-2, -1)
    assert result == -3


def test_multiply():
    result = calculator.multiply_numbers(1, 0)
    assert result == 0


def test_divide():
    result = calculator.divide_numbers(1, 0)
    assert result == False
