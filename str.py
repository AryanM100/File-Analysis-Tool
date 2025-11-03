#!/bin/python3

import sys

filename = sys.argv[1]
loc = "Text/str"
hexdata = ""
a = ""
b = ""
y = ""
final = ""
c = 0
d = 1
e = 0
f = 0

with open(filename, "rb") as file:
	for byte in file.read():
		hexdata += f"{byte:02x}"

for i in range(0, len(hexdata), 2):
	g = hexdata[i:i+2]
	try:
		bytearray.fromhex(g).decode()
	except:
		y += "."
	else:
		b = bytearray.fromhex(g).decode()
		if(b.isprintable() == True):
			y += b
		else:
			y += "."

while(f < len(y)):
	a = y[f]
	if(a == "."):
		f += 1
		continue
	while(c != 2):
		b = y[f+d]
		if(b == "."): 
			c += 1
			d += 1
		else:
			a += b
			d += 1

	e = len(a)
	f += d - 1
	d = 1
	c = 0
	if(e >= 4):
		final += a
		final += "\n"
	f += 1
	
with open(loc, "w") as file:
	file.write(final)