import random
import math
import unittest
from power_calc import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator(random.random()*100)
        print(self.calculator.value)

    def test_power(self):
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.power(1, 3).value,
                               calc_value * calc_value * calc_value)
        self.assertAlmostEqual(self.calculator.power(1, -2).value, 1/(calc_value * calc_value))
        self.calculator.value = 5
        self.assertEqual(self.calculator.power(1, 4, 1.5).value, 5*5*5*5*5*5)

    def test_root(self):
        calc_value = self.calculator.value
        self.assertAlmostEqual(self.calculator.root(1, 3).value, calc_value)
        self.calculator.value = calc_value
        self.assertAlmostEqual(self.calculator.root(2, -2).value, 1 / math.sqrt(math.sqrt(calc_value)))
        self.calculator.value = 2
        self.assertEqual(self.calculator.root(0.25).value, 16)


if __name__ == '__main__':
    unittest.main()