#!/bin/python3

import sys
import os

filetype = sys.argv[1]

file1 = "Text/exif"
file2 = "Text/binw"
file3 = "Text/wordsextracted"
file4 = "Text/lsb"
file5 = "Text/hex"
file6 = "Text/report"
file7 = "Text/strings"

print("\nA report summarizing analysis results has been generated and stored in Text/report.")

with open(file6, "w") as file:
	file.write(filetype)
	
	with open(file1) as f1:
		file.write("\n\n\nExiftool -\n")
		for line in f1:
			file.write(line)
		file.write("\n")
		
	with open(file2) as f2:
		file.write("\nBinwalk -\n")
		for line in f2:
			file.write(line)
		file.write("\n")
		
	if(filetype[14:18] == "JPEG" or filetype[14:17] == "PNG"):
		file.write("\nLSB Analysis -\n")
		if(os.stat(file4).st_size == 0):
				file.write("Image doesn't contain hidden data.\n\n")
		else:
			with open(file4) as f4:
				for line in f4:
					file.write(line)
				file.write("\n\n")
			
	with open(file3) as f3:
		file.write("\nExtracted Words -\n")
		for line in f3:
			file.write(line)
		file.write("\n")

#	with open(file7) as f7:
#		file.write("\nStrings -\n")
#		for line in f7:
#			file.write(line)			
#		file.write("\n")
#		
#	with open(file5) as f5:
#		file.write("\nHexdump -\n")
#		for line in f5:
#			file.write(line)