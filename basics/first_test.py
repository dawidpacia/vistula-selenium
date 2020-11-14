def calculate_fuel(mass):
    fuel = mass//3 - 2
    return fuel


def test_12():
    fuel = calculate_fuel(12)
    assert fuel == 2


def test_14():
    assert calculate_fuel(14) == 2


def test_1969():
    assert calculate_fuel(1969) == 654


def test_100756():
    assert calculate_fuel(100756) == 33583


def test_string():
    result = calculate_fuel("test")
    assert result == False


def test_negative_value():
    assert calculate_fuel(-10) == False