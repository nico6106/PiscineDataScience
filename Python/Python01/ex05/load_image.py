import numpy as np
from PIL import Image
import os


def ft_load(path: str) -> np.ndarray:
    """Function that load an image and returns its pixels as an RGB array"""
    try:
        if not type(path) is str:
            raise AssertionError('Incorrect path')
        if not path.lower().endswith(('jpg', 'jpeg')):
            raise AssertionError('Incorrect format')
        if not os.path.exists(path):
            raise AssertionError('File does not exist')
        img = Image.open(path)
        print(f"The shape of image is: {np.array(img).shape}")
        img_array = np.array(img)
        rgb_array = img_array[:, :, :3]
        print(rgb_array)
        return np.array(rgb_array)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
        return None
