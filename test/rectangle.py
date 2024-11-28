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

    def test_area_one(self):
        for _ in range(100):
            a = random.random()
            self.assertEqual(area(a, 1), a)
            self.assertEqual(area(1, a), a)

    def test_area_fract(self):
        self.assertEqual(area(1.2, 3.5), 4.2)

    def test_area_big(self):
        self.assertEqual(area(9476629010312086, 4328909928866542101), 41023473414924701476783193668132686)

    # PERIMITER

    def test_perimiter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimiter_line(self):
        for _ in range(100):
            a = random.random()
            self.assertEqual(perimeter(a, 0), a*2)

    def test_perimiter_fract(self):
        self.assertEqual(perimeter(2.33, 4.17), 13)

    def test_perimiter_big(self):
        self.assertEqual(perimeter(8422625216662349012, 2049844621679234781), 20944939676683167586)