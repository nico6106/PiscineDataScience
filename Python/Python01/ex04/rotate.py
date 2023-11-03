from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


ZOOM_IMG = 0.6


def show_image(img: np.ndarray):
    """show an image"""
    plt.imshow(img, cmap="gray")
    plt.show()
    return


def convert_grey(img: np.ndarray):
    """convert an image to a gray scale"""
    coefficients = np.array([0.299, 0.587, 0.114]).reshape(3, 1)
    newimg = np.dot(img[:, :, :], coefficients).round().astype(np.uint8)
    return newimg


def zoom(img: np.ndarray):
    """return an img afer zoom"""
    x = len(img[0])
    y = len(img)
    # sixe_x = int(np.trunc(x * ZOOM_IMG))
    # size_y = int(np.trunc(y * ZOOM_IMG))
    # start_x = max(0, x // 2 - sixe_x // 2)
    # start_y = max(0, y // 2 - size_y // 2)
    # sixe_x = sixe_x + start_x
    # size_y = size_y + start_y
    sixe_x = 400
    size_y = 400
    start_x = max(0, x // 2 - sixe_x // 2 - 50)
    start_y = max(0, y // 2 - size_y // 2 + 300)
    sixe_x = sixe_x + start_x
    size_y = size_y + start_y
    newimg = img[start_x:sixe_x, start_y:size_y]
    grayimg = convert_grey(newimg)
    return grayimg


def transpose_img(img: np.ndarray):
    """function that transpose an array given in argument"""
    array_2d = img[:, :, 0]
    newimg = np.zeros((len(array_2d[0]), len(array_2d)), dtype=int)
    for y in range(len(array_2d)):
        for x in range(len(array_2d[0])):
            newimg[x][y] = array_2d[y][x]
    return newimg


def main():
    """Main function or the program"""
    try:
        img = ft_load('animal.jpeg')
        newimg = zoom(img)
        print(f"The shape of image is: {np.array(newimg).shape} or \
({len(newimg)}, {len(newimg[0])})")
        print(newimg)
        transposed_img = transpose_img(newimg)
        print(f"New shape after Transpose: {np.array(transposed_img).shape}")
        print(transposed_img)
        show_image(transposed_img)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()
