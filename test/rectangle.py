import unittest
import random
from src.rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    # AREA

    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)
        for _ in range(100):
            self.assertEqual(area(random.random(), 0), 0)

    def test_area_fract(self):
        pass
