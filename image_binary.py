from PIL import Image
import numpy as np
import math

binary_data = input("please enter file: ")

# Open the binary file
with open(input, 'rb') as f:
    binary_data = f.read()

# Convert each byte to 8-bit binary string
bits = ''.join(format(byte, '08b') for byte in binary_data)

#dynamic x,y
num_bits = len(bits)
width = int(math.sqrt(num_bits))
height = num_bits // width

if num_bits % width != 0:
    height += 1

# Create numpy array for image data
img_data = np.zeros((height, width), dtype=np.uint8)  

# Fill image data based on bits
for i in range(len(bits)):
    y = i // width
    x = i % width
    img_data[y, x] = 173 if bits[i] == '1' else 0

# Create and save the image
img = Image.fromarray(img_data, mode='L')
img.save('binary_output.png')
print("Image saved as binary_output.png")
