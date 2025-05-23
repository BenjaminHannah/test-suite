import unittest
from src import triangle

class MyTestCase(unittest.TestCase):
    def test_something(self):

        #Provided by the sample file
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(0, 0, 0))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(-1, -2, -3))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 1, 3))
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(2, 2, 2))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(2, 2, 3))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(2, 3, 4))

        # 5.5.1 Test Cases for the Triangle Problem (Tests from the book)
        # Normal Boundary Value Test Cases
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(100, 100, 1))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(100, 100, 2))
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(100, 100, 100))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(100, 100, 199))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(100, 100, 200))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(100, 1, 100))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(100, 2, 100))
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(100, 100, 100))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(100, 199, 100))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(100, 200, 100))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(1, 100, 100))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(2, 100, 100))
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(100, 100, 100))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(199, 100, 100))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(200, 100, 100))
        # Does not have any scalene tests (above)

        # Weak Normal equivalence class test
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(5, 5, 5))

        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(2, 2, 3))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(2, 3, 2))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(3, 2, 2))

        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(3, 4, 5))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(3, 5, 4))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(5, 4, 3))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(5, 3, 4))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(4, 3, 5))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(4, 5, 3))

        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(4, 1, 2))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(4, 2, 1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(2, 4, 1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(2, 1, 4))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 4, 2))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 2, 4))

        # Decision Table-Based Testing
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(4, 1, 2))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 4, 2))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 2, 4))
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(5, 5, 5))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(2, 2, 3))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(2, 3, 3))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(3, 2, 2))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(3, 4, 5))

        # Previous Tests from Unit Testing Frameworks
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(1, 1, 1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 2, 1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 1, 2))
        self.assertEqual(triangle.SCALENE, triangle.triangle_identifier(4, 5, 6))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(4, 4, 6))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(4, 6, 4))
        self.assertEqual(triangle.ISOSCELES, triangle.triangle_identifier(4, 6, 6))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(0, 0, 0))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(-4, -4, -6))

        #Strong Tests
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(-1, 5, 5))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(5, -1, 5))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(5, 5, -1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(201, 5, 5))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(5, 201, 5))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(5, 5, 201))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(-1, -1, 5))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(-1, 5, -1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(5, -1, -1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(-1, -1, -1))

        #Extra tests
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(0, 0, 0))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(0.5, 0, 0))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 2, 3))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(1, 2, 3))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(2, 3, 1))
        self.assertEqual(triangle.INVALID, triangle.triangle_identifier(3, 1, 2))
        self.assertEqual(triangle.EQUILATERAL, triangle.triangle_identifier(7, 7, 7))


if __name__ == '__main__':
    unittest.main()
