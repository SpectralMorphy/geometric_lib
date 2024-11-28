import unittest
import math
from src.circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    # AREA

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_result_one(self):
        self.assertAlmostEqual(area(1/math.sqrt(math.pi)), 1)

    def test_area_large(self):
        self.assertAlmostEqual(area(74389901929460135821), 5533857509074696838237631522391767344041 * math.pi)

    # PERIMETER

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(perimeter(1), 2*math.pi)

    def test_perimeter_result_one(self):
        self.assertAlmostEqual(perimeter(0.5/math.pi), 1)

    def test_perimeter_large(self):
        self.assertAlmostEqual(perimeter(472910399747289102329837401), 945820799494578204659674802 * math.pi)