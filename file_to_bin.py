def file_to_binary(filepath):
    with open(filepath, 'rb') as f:
        byte_data = f.read()

    #convert each byte to an 8-bit string
    binary_str = ''.join(format(byte, '08b') for byte in byte_data)
    return binary_str

filename = input("enter path to file: ")
binary_content = file_to_binary(filename)
print(binary_content)

with open('out_bin.txt', 'w') as out_file:
    out_file.write(binary_content)
