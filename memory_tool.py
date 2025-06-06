import os
with open('custom-file-size.bin', 'wb') as f:
    f.write(os.urandom(259200))
