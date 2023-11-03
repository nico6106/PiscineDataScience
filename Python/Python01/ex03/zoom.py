from load_image import ft_load
# from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
# import cv2


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
    # methode PIL
    # newimg = Image.fromarray(newimg)
    # newimg = newimg.convert("L")
    # newimg = np.array(newimg)
    # methode CV2
    # newimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # methode calcul mano
    # newimg = np.zeros((len(img), len(img[0]), 1), dtype=np.uint16)
    # for y in range(len(img)):
    #     for x in range(len(img[0])):
    #         average = (img[y, x, 0] + img[y, x, 1] + img[y, x, 2]) // 3
    #         newimg[y][x][0] = average
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
# np.dot(newimg[:, :, :], [0.299, 0.587, 0.114]).round().astype(np.uint8)


def main():
    """Main function or the program"""
    try:
        img = ft_load('animal.jpeg')
        print(img)
        newimg = zoom(img)
        print(f"New shape after slicing: {np.array(newimg).shape} or \
({len(newimg)}, {len(newimg[0])})")
        print(newimg)
        show_image(newimg)
    except AssertionError as error:
        print(f"{AssertionError.__name__}: {error}")
    return


if __name__ == "__main__":
    main()
