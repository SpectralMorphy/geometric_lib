import unittest
import random
from src.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    # AREA

    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)
        
    def test_area_line(self):
        for _ in range(100):
            self.assertEqual(area(0, random.random()), 0)
            self.assertEqual(area(random.random(), 0), 0)

    def test_area_fract(self):
        self.assertEqual(area(1.2, 3.5), 4.2)
