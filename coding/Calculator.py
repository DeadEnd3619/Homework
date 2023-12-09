from main import Calculator

def test_calculator():
    calc = Calculator()

    assert calc.add(5, 3) == 8
    assert calc.add(-1, -1) == -2

    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, -1) == 0

    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10

    assert calc.divide(10, 2) == 5
    assert calc.divide(5, 0) is None

    assert calc.power(2, 3) == 8
    assert calc.power(-2, 3) == -8

    assert calc.modulus(10, 3) == 1
    assert calc.modulus(-10, 3) == 2

    assert calc.sqrt(9) == 3
    assert calc.sqrt(-1) is None

    assert calc.absolute(-5) == 5
    assert calc.absolute(5) == 5

    assert calc.factorial(5) == 120
    assert calc.factorial(-1) is None
    assert calc.factorial(4.5) is None

    print("All tests passed!")

test_calculator()
