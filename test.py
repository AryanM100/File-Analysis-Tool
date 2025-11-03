#!/bin/python3

<<<<<<< HEAD
import sys

filename = "Images/image.png"
loc = "Text/hex"

def main():
  hexdata = ""
  final = ""
  asc = ""
  y = ""
  c = 0
  d = 0
  e = 0
  last = 0
  
  with open(filename, "rb") as file:
    for byte in file.read():
      hexdata += f"{byte:02x}"
    
  for i in range(0, len(hexdata), 4):
    last += 1
    i = hexdata[i:i+4]
    asc += i
    if(e == 0):
      f = hex(d)
      f = f[2:]
      f = f.zfill(7) + "0"
      final += f + ": "
      d += 1
    e = 1
    
    final += i + " "
    c += 1
    if(c == 8 or last == (len(hexdata) / 4)):
      for j in range(0, len(asc), 2):
        g = asc[j:j+2]
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

      if(last == len(hexdata) / 4):
        length = 41 - (5 * len(asc)) / 4
        final += " " * int(length) + y
      else:
        final += " " + y
      if(last != len(hexdata) / 4):
        final += "\n"
      c = 0
      e = 0
      asc = ""
      y = ""

  return final

print("\nShow Hexdump ?")
a = input()
if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"): 
  z = main()
  print(z)
  with open(loc, "w") as file:
    file.write(z)
else:
  print("Stored in Text/hex.")
  z = main()
  with open(loc, "w") as file:
    file.write(z)

#rb
=======
loc = "Text/wow"
words = "Text/words1"
ex = "Text/wordsextracted"
string = ""
wor = ""

# print("\nDo you want to take an extensive check(consumes more time) of strings ?")
# a = input()
# if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"):
#   words = "Text/words2"

with open(words) as f:
  wor = f.read()
with open(loc) as file:
  string = file.read()

lines1 = wor.split("\n")
lines2 = string.split("\n")

with open(ex, "w") as fi:
  for line1 in lines1:
    for line2 in lines2:
      i = line2.lower().find(line1.lower())
      b = len(line1)
      if(i != -1):
        fi.write(line2[i:i+b])
        fi.write("\n")
            
print("Extracted Words -")

with open(ex) as file:
  for line in file:
    print(line, end="")
>>>>>>> 5e32295 (Removed absolute paths)
