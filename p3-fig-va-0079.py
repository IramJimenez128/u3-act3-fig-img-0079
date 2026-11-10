import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
#Iram Jimenez NC = 0079
print("Iram Jimenez NC = 0079")
print("UIII Act3 colocar puntos a una imagen en blanco y negro")
mi_imagen = cv2.imread("porfiriodiaz.jpeg")
plt.imshow(mi_imagen)
plt.title("Porfirio Diaz e Iram Jimenez 0079")
plt.show()
print("+-+-+-+-+-+-+-+- Puntos sobre la imagen +-+-+-+-+-+-+-+-")
plt.imshow(mi_imagen)
x = [100, 200, 500, 700]
y = [100, 300, 400, 200]
plt.scatter(x, y, s = 20, c = "Red")
plt.show()