import unittest
from math_quiz import random_integer_generator, sign_generator, math_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_sign_generator(self):
        all_signs = ['+', '-', '*']
        for _ in range(1000):
            sign = sign_generator()
            self.assertIn(sign, all_signs)

    def test_math_operation(self):

        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (1, 9, '*', '1 * 9', 9)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, real_answer = math_operation(num1, num2, operator)
            self.assertTrue(problem == expected_problem)
            self.assertTrue(real_answer == expected_answer)


if __name__ == "__main__":
    unittest.main()
