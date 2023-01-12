# File which will implement the IceCreamShoppe class
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by Quan Yuan
from Carton import Carton

class IceCreamShoppe:
    '''Class IceCreamShoppe
        Attributes: carton_radius, carton_height, cartons_used
        Methods: serve, cartonsUsed'''

    def __init__(self, carton_radius, carton_height):
        ''' Constructor
        Parameters: carton_radius, carton_height - dimensions for a carton
        Return: nothing'''
        self.carton_radius = carton_radius
        self.carton_height = carton_height
        self.cartons_used = 0
        self.carton = None

    def serve(self, numScoops, scooper):
        ''' serve method
        Parameters: numScoops - number of scoops wanted; 
            scooper - the specific Scoop to use
        Return: nothing'''
        # check whether there is previous opened carton
        if self.cartons_used == 0:
            self.carton = Carton(self.carton_radius, self.carton_height)
            self.cartons_used += 1
        
        for _ in range(numScoops):
            if self.carton.hasEnoughFor(scooper):
                self.carton.remove(scooper)
            else:
                self.carton = Carton(self.carton_radius, self.carton_height)
                self.cartons_used += 1
                self.carton.remove(scooper)

    def cartonsUsed(self):
        ''' cartonsUsed method
        Parameters: none
        Return: the number of cartons used so far in the Shoppe'''
        return self.cartons_used