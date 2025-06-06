from PIL import Image
import math

binary_data = input("please put file: ")

with open (binary_data, 'rb') as f:
    binary_data = f.read()

if not all(c in'01' for c in binary_data):
       binary_data = ''.join(format(ord(c), '08b') for c in binary_data)

chunks = [binary_data[1:1+3] for i in range(0, len(binary_data), 3)]

# color mapping
colors = {
        '000': (0, 0, 0),        #black
        '001': (255, 255, 255),  #white
        '010': (255, 0, 0),      #red
        '011': (0, 255, 0),      #green
        '100': (0, 0, 255),      #blue
        '101': (255, 255, 0),    #yellow
        '110': (0, 255, 255),    #cyan
        '111': (255, 0, 255)     #megenta
}

if len(chunks) == 0:
    print("Files empty Dumbass")
    exit(1)
num_chunks = len(chunks)
side = math.ceil(math.sqrt(num_chunks))

img = Image.new('RGB', (side, side), color=(0, 0, 0))

for i, bits in enumerate(chunks):
    if len(bits) < 3:
        bits = bits.ljust(3, '0')
    x = i % side
    y = i // side
    img.putpixel((x, y), colors[bits])

img.save('color_encoded.png')
print("Created: color_encoded.png")
img.show('color_encoded.png')
