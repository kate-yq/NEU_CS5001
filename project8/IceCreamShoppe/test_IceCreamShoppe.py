# Quan Yuan
# Nov 25, 2022

from IceCreamShoppe import IceCreamShoppe
from Scoop import Scoop
import unittest

class IceCreamTest(unittest.TestCase):
    def test_init(self):
        iceCream = IceCreamShoppe(3, 4)
        self.assertAlmostEqual(iceCream.carton_radius, 3)
        self.assertAlmostEqual(iceCream.carton_height, 4)
        self.assertEqual(iceCream.cartons_used, 0)

    def test_serve(self):
        iceCream = IceCreamShoppe(3, 4)
        s1 = Scoop(2)
        iceCream.serve(3, s1)
        self.assertEqual(iceCream.cartons_used, 1)
        iceCream.serve(5, s1)
        self.assertEqual(iceCream.cartons_used, 3)



def main():
    unittest.main()

if __name__ == "__main__":
    main()