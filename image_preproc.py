import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
i = misc.ascent()
plt.grid(False)

def conv(i, filter, weight):

    for x in range(1, size_x - 1):
        for y in range(1, size_y - 1):
            convolution = 0.0
            convolution = convolution + (i[x - 1, y - 1] * filter[0][0])
            convolution = convolution + (i[x, y - 1] * filter[0][1])
            convolution = convolution + (i[x + 1, y - 1] * filter[0][2])
            convolution = convolution + (i[x - 1, y] * filter[1][0])
            convolution = convolution + (i[x, y] * filter[1][1])
            convolution = convolution + (i[x + 1, y] * filter[1][2])
            convolution = convolution + (i[x - 1, y + 1] * filter[2][0])
            convolution = convolution + (i[x, y + 1] * filter[2][1])
            convolution = convolution + (i[x + 1, y + 1] * filter[2][2])
            convolution = convolution * weight
            if (convolution < 0):
                convolution = 0
            if (convolution > 255):
                convolution = 255
            i_transformed[x, y] = convolution
    return i_transformed

i_transformed = np.copy(i)

size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

print(size_x)
print(size_y)

filter = [ [-1, -1, -1],
           [-1, 8, -1],
           [-1, -1, -1]]

filter = [ [-1, -1, 0],
           [-1, 0, 1],
           [0, 1, 1]]




#filter1 = [[-1, -1, -1], [0,0,0], [1,1,1]]
weight = 2

i_transformed = conv(np.copy(i), filter, weight)



plt.imshow(i_transformed)
plt.show()