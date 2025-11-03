#!/bin/python3

loc = "Text/str"
<<<<<<< HEAD
words = "Wordlists/words1"
=======
words = "Text/words1"
>>>>>>> 5e32295 (Removed absolute paths)
ex = "Text/wordsextracted"
string = ""
wor = ""

print("\nDo you want to take an extensive check(consumes more time) of strings ?")
a = input()
if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"):
<<<<<<< HEAD
  words = "Wordlists/words2"
=======
  words = "Text/words2"
>>>>>>> 5e32295 (Removed absolute paths)

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