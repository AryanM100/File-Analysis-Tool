#!/bin/python3

from PIL import Image
import sys

filename = sys.argv[1]
loc = "Text/lsb"

print("\nLSB Analysis -")

img = Image.open(filename)
pixels = img.load()

binm = ""
decm = ""

for i in range(img.height):
  for j in range(img.width):
    r, g, b = pixels[j, i]
    binm += str(r & 1)
    binm += str(g & 1)
    binm += str(b & 1)
    
for i in range(0, len(binm), 8):
	e = binm[i:i+8]
	if(len(e) == 8):
		decm += chr(int(e, 2))

decm = decm.split("\x00")[0]

if(len(decm) == 0):
	print("Image doesn't contain hidden data.")
else:
	print(decm)

with open(loc, "w") as file:
<<<<<<< HEAD
	file.write(decm)
=======
	file.write(decm)

#1 import
#2 import & main()
#3 fat -> file -> lsb
#4 subprocess.run()
>>>>>>> 5e32295 (Removed absolute paths)
