from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def show_image(img: np.ndarray):
    """show an image"""
    plt.imshow(img)
    plt.show()
    return


def zoom(img: np.ndarray, start_x, start_y, sixe_x, size_y):
    """return an img afer zoom"""
    newimg = img[start_x:sixe_x, start_y:size_y,]
    return newimg


def main():
    """Main function or the program"""
    try:
        img = ft_load('animal.jpeg')
        print(img)
        newimg = zoom(img, 400, 50, 400, 400)
        print(f"The shape of image is: {np.array(newimg).shape}")
        print(newimg)
        show_image(newimg)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()
