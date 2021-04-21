# realQuadratic.py
# Copyright (c) 2020-2021 Drew Markel


def realQuadratic(variableA=1, variableB=1, variableC=1) -> tuple:
    """
    Calculates solutions for a quadratic formula
    variableA: Ax^2 (int|float|complex)
    variableB: Bx (int|float|complex)
    variableC: C (int|float|complex)
    """
    inverseB = (-variableB)
    discriminant = ((variableB**2) - (4 * variableA * variableC))
    denominator = (2 * variableA)
    if variableA == 0:
        raise ZeroDivisionError
    else:
        solutionA = ((inverseB - (discriminant**0.5)) / denominator)
        solutionB = ((inverseB + (discriminant**0.5)) / denominator)
        return solutionA, solutionB
