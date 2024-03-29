#coding: utf-8
import ctypes
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

testlib = ctypes.CDLL('./blackboard.so') #chama a lybrary que contem as funções em c++
testlib.using_shared_memory()   #usando a função do c++
testlib.leitura_int.restype = ctypes.c_int #define o tipo de retorno da função, neste caso a função retorna int

index = 2
image = np.zeros([testlib.leitura_int(1),testlib.leitura_int(0),3])
for y in range(testlib.leitura_int(0)):
    for x in range(testlib.leitura_int(1)):
        image[x,y,0] = testlib.leitura_int(index)   #B
        image[x,y,1] = testlib.leitura_int(index+1) #G
        image[x,y,2] = testlib.leitura_int(index+2) #R
        index = index + 3
          
# cv2.imwrite('color_img.jpg', image)
cv2.imshow("image", image);
cv2.waitKey();
