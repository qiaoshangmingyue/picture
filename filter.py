
import cv2 as cv
import numpy as np
import math
import copy


def gaussion_box(a, p):
    gauss = np.zeros((a, a))
    suma = 0
    for i in range(0, a):
        for j in range(0, a):
            t = (i-(a-1)/2)**2+(j-(a-1)/2)**2
            gauss[i][j] = math.e ** (-t/(2*p*p))
            suma = suma + gauss[i][j]
    gauss = gauss/suma
    return gauss


def gauss_tras(img, a, gauss):
    img0 = copy.copy(img)

    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if i > (a-1)/2-1 and j > (a-1)/2-1 and i < img.shape[0]-(a-1)/2 and j < img.shape[1]-(a-1)/2:
                sum1 = 0
                for m in range(0, a):
                    for n in range(0, a):
                        sum1 += img[int(i-(a-1)/2+m)][int(j-(a-1)/2+n)]*gauss[m][n]
                img0[i][j] = sum1
    return img0

def average(img, a):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if i > (a-1)/2-1 and j > (a-1)/2-1 and i < img.shape[0]-(a-1)/2 and j < img.shape[1]-(a-1)/2:
                sum1 = []
                for m in range(0, a):
                    for n in range(0, a):
                        sum1.append(img[int(i-(a-1)/2+m)][int(j-(a-1)/2+n)])
                img0[i][j] = np.average(sum1)
    return img0

def median(img, a):
    img0 = copy.copy(img)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if i > (a-1)/2-1 and j > (a-1)/2-1 and i < img.shape[0]-(a-1)/2 and j < img.shape[1]-(a-1)/2:
                sum1 = []
                for m in range(0, a):
                    for n in range(0, a):
                        sum1.append(img[int(i-(a-1)/2+m)][int(j-(a-1)/2+n)])
                img0[i][j] = np.median(sum1)
    return img0


def main():
    a = [3, 5, 9]
    for j in range(1, 9):
        if j==2 or j == 4:
            img0 = cv.imread(r"D:\onedrive\pythonProject\{0}.png".format(j))
        else:
            img0 = cv.imread(r"D:\onedrive\pythonProject\{0}.jpg".format(j))
        for i in range(3):
            gauss = gaussion_box(a[i], 10)

            gauss_img = gauss_tras(copy.copy(img0), a[i], gauss)
            average_img = average(copy.copy(img0), a[i])
            median_img = median(copy.copy(img0), a[i])
            cv.imwrite(r"./result/guassian_img{0}_{1}x{1}.jpg".format(j, a[i]), gauss_img)
            cv.imwrite(r"./result/average_img{0}_{1}x{1}.jpg".format(j, a[i]), average_img)
            cv.imwrite(r"./result/median_img{0}_{1}x{1}.jpg".format(j, a[i]), median_img)
            print(i)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
