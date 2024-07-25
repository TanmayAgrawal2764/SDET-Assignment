import unittest
from Part1 import is_prime, calculate_discount
#Here we have used the unittest module to test the functions separately as separate units.
class TestFunctions(unittest.TestCase):

    # Test cases for is_prime function
    def test_is_prime(self):
        self.assertTrue(is_prime(2))#check for first prime number
        self.assertTrue(is_prime(3))#check for first odd prime number
        self.assertFalse(is_prime(1))#check for first non-prime number
        self.assertFalse(is_prime(0))#check for invalid-prime/zero number
        self.assertFalse(is_prime(-1))#check for negative number
        self.assertFalse(is_prime(4))#check for first non-prime number
        self.assertTrue(is_prime(13))#check for normal random prime number
        self.assertFalse(is_prime(100000000))#check for large number

    # Test cases for calculate_discount function
    def test_calculate_discount(self):
        self.assertEqual(calculate_discount(100, 10), 90)#case for normal discount
        self.assertEqual(calculate_discount(200, 0), 200)#case for zero discount
        self.assertEqual(calculate_discount(100, 100), 0)#case for full discount
        self.assertEqual(calculate_discount(10000000, 10), 9000000)#case for high price
        with self.assertRaises(ValueError):#case for negative discount
            calculate_discount(100, -10)
        with self.assertRaises(ValueError):#case for negative price
            calculate_discount(-100, 10)
        with self.assertRaises(ValueError):#case for discount higher than price itself
            calculate_discount(100, 110)
        with self.assertRaises(ValueError):#case for invalid data type of price input as string
            calculate_discount("100", 10)
        with self.assertRaises(ValueError):#case for invalid data type of discount input as string
            calculate_discount(100, "10")
        with self.assertRaises(ValueError):#case for invalid data type of both inputs as string
            calculate_discount("100", "10")

if __name__ == "__main__":
    unittest.main()