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
print("+-+-+-+-+-+-+-+- Cuadro azul en la imagen +-+-+-+-+-+-+-+-")
imagenez = cv2.imread("emiliozapata.jpg")
plt.imshow(imagenez)
x = [100, 100, 400, 400, 100]
y = [400, 100, 100, 400, 400]
plt.plot(x, y, c = "blue")
plt.show()
print("+-+-+-+-+-+-+-+- Cuadro verde en la imagen +-+-+-+-+-+-+-+-")
imagenez = cv2.imread("emiliozapata.jpg")
plt.imshow(imagenez)
N= 30
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc, yc) = (240, 220)
r = 150
for i in range(N+1):
  t     = 2*np.pi/N*i
  x[i]  = xc + r*np.cos(t)
  y[i]  = yc + r*np.sin(t)
plt.plot(x, y, c = "Green")
plt.show()