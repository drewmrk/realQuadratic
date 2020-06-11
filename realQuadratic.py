# realQuadratic.py
# Copyright (c) 2020 Drew Markel

# Import math packages
from math import pow

# Create "realQuadratic" class
class realQuadratic:

    # Grab variables
    def __init__(self, variableA, variableB, variableC):
        # Declare variables
        self.variableA = variableA
        self.variableB = variableB
        self.variableC = variableC
        # Take the "opposite" of variableB
        self.inverseB = (-variableB)
        # Calculate the discriminant
        self.discriminant = (pow(variableB, 2) - (4 * variableA * variableC))
        # Calculate the denominator
        self.denominator = (2 * variableA)

    # Calculate solution(s)
    def solution(self, number):
        # Check to make sure A is not zero
        if self.variableA == 0:
            return "Error: Cannot divide by zero."
        else:
            # Return first solution
            if number == 1:
                return ((self.inverseB - (self.discriminant ** 0.5)) / self.denominator)
            # Return second solution
            elif number == 2:
                return ((self.inverseB + (self.discriminant ** 0.5)) / self.denominator)
            # Return if the program failed
            else:
                return "An unknown error occurred."