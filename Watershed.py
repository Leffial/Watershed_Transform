import matplotlib.pyplot as plt
import cv2


def main():
    folder = "tumbnail.jpg"

    imgfolder1 = folder + "gray21.512.tiff"
    img = cv2.imread(imgfolder1,1)

    th = 127
    max_val = 255

    ret,o1 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY)
    ret,o2 = cv2.threshold(img, th, max_val, cv2.THRESH_BINARY_INV)
    ret,o3 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO)
    ret,o4 = cv2.threshold(img, th, max_val, cv2.THRESH_TOZERO_INV)
    ret,o5 = cv2.threshold(img, th, max_val, cv2.THRESH_TRUNC)

    output = [img, o1, o2, o3, o4, o5]

    titles = ['Original', 'Binary', 'Binary_inv', 'Zero', 'Zero_inv', 'Trunc']

    for i in range(6):
        plt.subplot(2,3, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
