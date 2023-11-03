import numpy as np


def verif_arg(family: list, start: int, end: int) -> bool:
    """verif is arguments are correct -> bool"""
    if not type(family) is list:
        print("First argument must be a list")
        return False
    if not (type(start) is int and type(end) is int):
        print("Start/End must be integer")
        return False
    if not all(len(item) == len(family[0]) for item in family):
        print("Lists size cannot be differents")
        return False
    # if len(family) > 0:
    #     init_size = len(family[0])
    #     for elem in family:
    #         if len(elem) != init_size:
    #             print("Lists size cannot be differents")
    #             return False
    return True


def slice_me(family: list, start: int, end: int) -> list:
    """function to slice the family argument using start and end"""
    if not verif_arg(family, start, end):
        return []
    print(f"My shape is : {np.array(family).shape}")
    new_list = np.array(family)[start:end].tolist()
    print(f"My new shape is : {np.array(new_list).shape}")
    return new_list
