#!/bin/python3

loc = "/home/ryan/IS/WOC/2strings"
words = "/home/ryan/IS/WOC/words1"
ex = "/home/ryan/IS/WOC/wordsextracted"
string = ""
wor = ""

print("\nDo you want to take an extensive check(consumes more time) of strings ?")
a = input()
if(a == "Y" or a == "y" or a == "yes" or a == "Yes" or a == "YES"):
  words = "/home/ryan/IS/WOC/words2"

with open(ex, "w") as fi:
  with open(loc) as file:
    for string in file:
      with open(words) as f:
        for wor in f:
          i = string.lower().find(wor.lower())
          b = len(wor)
          if(i != -1):
            fi.write(string[i:i+b])
            
print("Extracted Words -")

with open(ex) as file:
  for line in file:
    print(line, end="")