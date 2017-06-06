from PIL import Image
import numpy as np
class Converter:
    def convert_to_alpha_list(self, decode_str):
        img = Image.frombytes(data=decode_str, size=(250, 250), mode='RGBA')
        pixels = img.resize((28, 28)).tobytes("raw", "A")

        temp = np.array([i for i in pixels])
        temp = temp.reshape(28, 28)

        for i in range(temp.shape[0]):
            for j in range(temp.shape[1]):
                print("{:4}".format(temp[i, j]), end='')
            print()
        return np.array([pixel / 255 for pixel in pixels]).reshape(1, 784)