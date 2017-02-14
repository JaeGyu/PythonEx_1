import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./room.jpg')
plt.imshow(img)
plt.show()
