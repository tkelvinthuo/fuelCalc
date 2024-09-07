"""
Unittests for the Fuel Calculator program testing edge cases
"""

import unittest
from unittest.mock import patch
from io import StringIO
from main import get_input, fuel_type, total_cost

class TestFuelCalc(unittest.TestCase):
    @patch('builtins.input', return_value='a')
    def test_get_input(self, mock_input):
        self.assertEqual(get_input("Enter fuel type: ", ['a', 'b']), 'a')

    @patch('builtins.input', side_effect=['c', 'a'])
    @patch('sys.stdout', new_callable=StringIO)

    def test_get_input_invalid_then_valid(self, mock_stdout, mock_input):
        result = get_input("Enter fuel type: ", ['a', 'b'])
        self.assertEqual(result, 'a')
        self.assertIn("Invalid choice", mock_stdout.getvalue())

    @patch('builtins.input', return_value='a')
    def test_fuel_type(self, mock_input):
        self.assertEqual(fuel_type(), 'a')

    def test_total_cost(self):
        self.assertEqual(total_cost(10, 'a'), 1880)
        self.assertEqual(total_cost(10, 'b'), 1700)
        self.assertEqual(total_cost(15, 'a'), 2820)
        self.assertEqual(total_cost(15, 'b'), 2550)

if __name__ == "__main__":
   unitest.main()
