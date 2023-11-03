import numpy as np
from matplotlib import pyplot as plt


def show_image(img: np.ndarray):
    """show an image"""
    plt.imshow(img, cmap="gray")
    plt.show()
    return


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    if (array is None):
        return
    newimg = np.zeros_like(array)
    newimg = 255 - array
    show_image(newimg)
    return


def ft_red(array) -> np.ndarray:
    """modify an image with a red scale color"""
    if (array is None):
        return
    newimg = np.zeros_like(array)
    for y in range(len(array)):
        for x in range(len(array[0])):
            newimg[y][x][0] = array[y][x][0]
    show_image(newimg)
    return


def ft_green(array) -> np.ndarray:
    """modify an image with a green scale color"""
    if (array is None):
        return
    newimg = np.zeros_like(array)
    for y in range(len(array)):
        for x in range(len(array[0])):
            newimg[y][x][1] = array[y][x][1]
    show_image(newimg)
    return


def ft_blue(array) -> np.ndarray:
    """modify an image with a blue scale color"""
    if (array is None):
        return
    newimg = np.zeros_like(array)
    newimg[:, :, 2] = array[:, :, 2]
    show_image(newimg)
    return


def ft_grey(array) -> np.ndarray:
    """modify an image with a gray scale color"""
    if (array is None):
        return
    newimg = array[:, :, 2]
    # for y in range(len(array)):
    #     for x in range(len(array[0])):
    #         newimg[y][x][0] = array[y][x][0] / 255
    #         newimg[y][x][1] = array[y][x][1] / 255
    #         newimg[y][x][2] = array[y][x][2] / 255
    # average = array[y][x][0] + array[y][x][1] + array[y][x][2]
    # newimg[y][x] = average / 3
    show_image(newimg)
    return
