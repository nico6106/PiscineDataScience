import numpy as np
import os
import pandas as pd



def load(path: str) -> pd.DataFrame:
    """Function that loads the data from path argument"""
    try:
        if not type(path) is str:
            raise AssertionError('Incorrect path')
        if not path.lower().endswith('csv'):
            raise AssertionError('Incorrect format')
        if not os.path.exists(path):
            raise AssertionError('File does not exist')
        bb_data = pd.read_csv(path)
        print(f"Loading dataset of dimensions {np.array(bb_data).shape}")
        return bb_data
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None