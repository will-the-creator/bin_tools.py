from PIL import Image 
filename = input("file name: ")
img = Image.open(filename).convert('L') #convert to grey
pixels = img.load()
width, height = img.size
binary_data = ''
for y in range(height):
    for x in range(width):
        pixel_value = pixels[x, y]
        if pixel_value > 128: #please adjust
            binary_data += '1'
        else:
            binary_data += '0'

print(binary_data)

with open('final_binary.txt', 'w') as f:
    f.write(binary_data)
