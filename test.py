import unittest
from area_lib import triangle_area, is_triangle_right, cirlce_area
from math import pi

class TestArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(triangle_area(3), pi*3**2)
        self.assertEqual(triangle_area(111), pi*111**2)
        self.assertEqual(triangle_area(0), pi*0**2)
        self.assertEqual(triangle_area(2.1), pi*2.1**2)
        self.assertEqual(triangle_area(pi), pi*pi**2)