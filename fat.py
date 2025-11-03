#!/bin/python3

def main():
	import argparse
	import subprocess

	parser = argparse.ArgumentParser(description = "This is a File Analysis Tool, with which you can do the following -\n"
													"1. Run this on a file.\n"
													"2. Use a new custom method to hide data in an image.")
	parser.add_argument("-f", metavar="", help="For running on a file.", type=str)
<<<<<<< HEAD
=======
# parser.add_argument("-d", metavar="", help="For running on a directory.", type=str)
>>>>>>> 5e32295 (Removed absolute paths)
	parser.add_argument("-e", metavar="", help="For hiding data in an image using a new custom way.", type=str)
	args = parser.parse_args()

	loc1 = args.f
<<<<<<< HEAD
=======
# loc2 = args.d
>>>>>>> 5e32295 (Removed absolute paths)
	loc3 = args.e

	file1 = "file.py"
	file2 = "strings.py"
	file3 = "lsb.py"
	file4 = "lsb"
	file5 = "custom.py"

	if(loc1 == None and loc3 == None):
		print("Use this tool with an option. Use -h or --help for help.")

	elif(loc1 != None):
		subprocess.call(['bash', './file.sh', loc1])
				
		result = subprocess.run(['python3', 'file.py'], input=loc1, text=True, capture_output=True)
		lsb = result.stdout.strip()
		print(lsb)
		
		subprocess.call(['python3', 'str.py', loc1])

		subprocess.call(['bash', './binw.sh', loc1])
		
		subprocess.call(['python3', 'hex.py', loc1])
		
		if(lsb[14:18] == "JPEG" or lsb[14:17] == "PNG"):
			subprocess.call(['python3', 'lsb.py', loc1])
		else:
			with open(file4, 'w') as file: 
				pass

		print("\nDo you want to run steghide ?")
		a = input()
		if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"):
			subprocess.call(['bash', './steg.sh', loc1])

		with open(file2) as file:
			exec(file.read())
			
		subprocess.call(['python3', 'report.py', lsb])
	
	elif(loc3 != None):
		subprocess.call(['python3', 'custom.py', loc1])

if __name__ == "__main__":
	main()