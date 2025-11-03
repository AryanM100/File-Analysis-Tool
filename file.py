#!/bin/python3

import sys

filename = sys.stdin.read().strip()

loc = "Text/xxd"
a = ""

j = "ffd8 ffe0 0010 4a46"   #jpg
p = "8950 4e47 0d0a 1a0a"   #png
t = "7573 7461 7200 3030"   #tar
bz = "425a 68"              #bzip2
gz = "1f8b"                 #gzip
z7 = "377a bcaf 271c"       #7z
z = "504b 0304"             #zip
mp0 = "4944 33"
mp1 = "fffb"                #mp3
mp2 = "fff3"                #mp3
mp3 = "fff2"             
w = "5249 4646 ???? ???? 5741 5645"    #wav
webp = "5249 4646 ???? ???? 5745 4250" #webp
mp4 = "6674 7970 4d53 4e56" #mp4
mp5 = "6674 7970 6973 6f6d" #mp4
pdf = "2550 4446 2d"        #pdf
txt0 = "efbb bf"           
txt1 = "fffe"               
txt2 = "feff"			          #text
txt3 = "fffe 0000"          #text
txt4 = "0000 feff"
txt5 = "0efe ff"

with open(loc) as file:
  for i in range(1,50):
    a += file.read(1)

b = a[10:]

if(b[:19] == j):
  print("File Format : JPEG Image Data")
elif(b[:19] == p):
  print("File Format : PNG Image Data")
elif(b[:19] == t):
  print("File Format : Tar Compressed Data")
elif(b[:7] == bz):
  print("File Format : Bzip2 Compressed Data")
elif(b[:4] == gz):
  print("File Format : Gzip Compressed Data")
elif(b[:14] == z7):
  print("File Format : 7-zip Archive Data")
elif(b[:9] == z):
  print("File Format : Zip Archive Data")
elif(b[:7] == mp0 or b[:4] == mp1 or b[:4] == mp2 or b[:4] == mp3):
  print("File Format : MP3 Audio")
elif(b[:9] == w[:9] and b[20:29] == w[20:29]):
  print("File Format : WAVE Audio")
elif(b[:9] == webp[:9] and b[20:29] == webp[20:29]):
  print("File Format : WebP Image Data")
elif(b == mp4 or b == mp5):
  print("File Format : MP4 Video")
elif(b[:12] == pdf):
  print("File Format : PDF Document")
elif(b[:7] == txt0 or b[:4] == txt1 or b[:4] == txt2 or b[:9] == txt3 or b[:9] == txt4 or b[:7] == txt5):
  print("File Format : Text File")
else:
  print("File Format : Not Recognized")