'''
image - матрица.
    серые цвета - Т.е. значения матрицы лежат в интервале от 0 до 255.
    image.shape = (2*m, 2*n)
mask - одномерный numpy array (вектор), маска для вычисления скалярного умножения, mask.shape = (m*n, ).
Выход
    скалярное произведение вектора маски mask и вектора
    image_vect - результата применения к матрице image операции
    max_pooling 2х2 и функции flatten() (превращение матрицы в строку).
'''
import numpy as np


def maxpooling_2x2(image, mask):
    m, n = image.shape
    pooling_2x2 = []
    for row in np.vsplit(image, m /2):
        for col in np.hsplit(row, n /2):
            pooling_2x2.append(col.max())
    pooling_2x2 = np.array(pooling_2x2)
    return pooling_2x2 @ mask


if __name__ == '__main__':
    image = np.array([[1,0,2,3], [4,6,6,8], [3,1,1,0], [1,2,2,4]])
    print(maxpooling_2x2(image, np.array([1,-1,-1,1])))