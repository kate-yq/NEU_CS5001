# Quan Yuan
# Nov 25, 2022

from Carton import Carton
from Scoop import Scoop
import unittest
import math

class CartonTest(unittest.TestCase):
    def test_init(self):
        can = Carton(2, 3)
        exp = 12 * math.pi
        self.assertAlmostEqual(can.contains, exp)

    def test_enough(self):
        can = Carton(2, 3)
        s1 = Scoop(2)
        s2 = Scoop(3)
        self.assertTrue(can.hasEnoughFor(s1))
        self.assertFalse(can.hasEnoughFor(s2))

    def test_remove(self):
        can = Carton(3, 4)
        s1 = Scoop(3)
        can.remove(s1)
        self.assertAlmostEqual(can.contains, 0)


def main():
    unittest.main()

if __name__ == "__main__":
    main()