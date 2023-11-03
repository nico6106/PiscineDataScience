import numpy as np


def verif_list_content(lst: list[int | float]) -> bool:
    """check if list only contains integers or floats values"""
    for elem in lst:
        # print(elem, type(elem))
        if not (type(elem) is int or type(elem) is float):
            return False
        if elem < 0:
            return False
    return True


def give_bmi(height: list[int | float], weight: list[int | float])\
 -> list[int | float]:
    """function that give a list of BMI values
    returns an assemption error if wrong arguments"""
    try:
        if (not (type(height) is list)):
            raise AssertionError("Args must be lists of int or floats")
        if not (verif_list_content(height) and verif_list_content(weight)):
            raise AssertionError("Args must be lists\
                                  of positives int or floats")
        if not (len(height) == len(weight)):
            raise AssertionError("List does not have the same length")
        height_square = np.multiply(height, height)
        new = np.divide(weight, height_square)
        new = new.tolist()
        return new
    except Exception as error:
        print(f"Error: {error}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """function that applies limits to the list"""
    try:
        if (not (type(bmi) is list)):
            raise AssertionError("BMI must be lists of int or floats")
        if not (type(limit) is int or type(limit) is float):
            raise AssertionError("Limit must be an int or a float")
        if not (verif_list_content(bmi)):
            raise AssertionError("BMI must be a list\
                                  of positives int or floats")
        bmi_array = np.array(bmi)
        greater_than_threshold = bmi_array > limit
        greater_than_threshold = list(greater_than_threshold)
        return greater_than_threshold
    except Exception as error:
        print(f"Error: {error}")
        return []
