import unittest
from src.square import area, perimeter

class SquareTestCase(unittest.TestCase):

    # AREA

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_one(self):
        self.assertEqual(area(1), 1)

    def test_area_nine(self):
        self.assertEqual(area(9), 81)

    def test_area_fract(self):
        self.assertEqual(area(1.5), 2.25)

    def test_area_big(self):
        self.assertEqual(area(48120937192873403), 2315624596320466786677371584800409)

    # PERIMETER

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_fract(self):
        self.assertEqual(perimeter(2.5), 10)

    def test_perimeter_big(self):
        self.assertEqual(perimeter(234098120398474839210136), 936392481593899356840544)