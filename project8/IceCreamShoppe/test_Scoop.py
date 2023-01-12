# Quan Yuan
# Nov 25, 2022

from Scoop import Scoop
import unittest
import math

class ScoopTest(unittest.TestCase):
    def test_init(self):
        s1 = Scoop(2)
        self.assertAlmostEqual(s1.radius, 2)

    def test_volume(self):
        s1 = Scoop(2)
        exp = 4 / 3 * 8 * math.pi
        self.assertAlmostEqual(s1.volume(), exp)


def main():
    unittest.main()

if __name__ == "__main__":
    main()
