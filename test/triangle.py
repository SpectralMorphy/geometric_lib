import unittest
import random
from src.triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    #AREA

    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)

    def test_area_line(self):
        for _ in range(100):
            self.assertEqual(area(0, random.random()), 0)
            self.assertEqual(area(random.random(), 0), 0)

    def test_area_one(self):
        self.assertEqual(area(1,1), 0.5)

    def test_area_fract(self):
        self.assertEqual(area(5.21, 7.2), 18.756)

    def test_area_big(self):
        self.assertEqual(area(32409813791923842, 98472871823787471), 1595743719682467937160122012891791)

    # PERIMETER

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_one(self):
        self.assertEqual(perimeter(1,1,1), 3)

    def test_perimeter_fract(self):
        self.assertEqual(perimeter(3.21, 7.47, 4.32), 15)

    def test_perimeter_big(self):
        self.assertEqual(perimeter(79812413289784167109375, 47802213201057892303, 234897329140203749283), 80095112832125428750961)