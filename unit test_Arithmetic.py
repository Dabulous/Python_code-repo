import unittest
from Arithmetic import calculate_numbers
from io import StringIO
import sys

class TestCalculateNumbers(unittest.TestCase):

    def test_sum(self):
        # Test sum calculation
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        calculate_numbers()
        sys.stdout = sys.__stdout__
        self.assertIn("Sum:", capturedOutput.getvalue())

    def test_difference(self):
        # Test difference calculation
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        calculate_numbers()
        sys.stdout = sys.__stdout__
        self.assertIn("Difference:", capturedOutput.getvalue())

    def test_quotient(self):
        # Test quotient calculation
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        calculate_numbers()
        sys.stdout = sys.__stdout__
        self.assertIn("Quotient:", capturedOutput.getvalue())

    def test_product(self):
        # Test product calculation
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        calculate_numbers()
        sys.stdout = sys.__stdout__
        self.assertIn("Product:", capturedOutput.getvalue())

    def test_division_by_zero(self):
        # Test division by zero
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        calculate_numbers()
        sys.stdout = sys.__stdout__
        self.assertIn("Error: Division by zero", capturedOutput.getvalue())

if __name__ == '__main__':
    unittest.main()