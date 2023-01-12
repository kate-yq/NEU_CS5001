# File which will hold the main function for the IceCreamShoppe project
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Quan Yuan
from IceCreamShoppe import IceCreamShoppe
from Carton import Carton
from Scoop import Scoop

def main():
    # ask for 2 scoops radius
    r1 = float(input("What is the radius of your first scooper? "))
    scoop1 = Scoop(r1)
    r2 = float(input("What is the radius of your second scooper? "))
    scoop2 = Scoop(r2)

    # ask for radius and height of carton
    r = float(input("What is the radius of your carton? "))
    h = float(input("What is the height of your carton? "))
    iceCreamShoppe = IceCreamShoppe(r, h)

    more = input("Would you like more ice cream? (Enter 1 for yes and 0 for no) ")
    while more == '1':
        num_scoop1 = int(input(f"How many {r1} scoops would you like? "))
        iceCreamShoppe.serve(num_scoop1, scoop1)
        num_scoop2 = int(input(f"How many {r2} scoops would you like? "))
        iceCreamShoppe.serve(num_scoop2, scoop2)
        more = input("Would you like more ice cream? (Enter 1 for yes and 0 for no) ")
    
    print(f"You used {iceCreamShoppe.cartonsUsed()} cartons of ice cream.")




if __name__ == "__main__":
    main()