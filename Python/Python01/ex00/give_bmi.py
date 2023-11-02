import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float])\
 -> list[int | float]:
    """function that give a list of BMI values
    returns an assemption error if wrong arguments"""
    print(type(height))
    if (not (type(height) is list or type(height) is float)):
        raise AssertionError("Types must be lists of int or floats")
    return


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """function that applies limits to the list"""
    return
