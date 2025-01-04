#!/bin/bash

filename=$(echo $1)

xxd $filename > /home/ryan/IS/WOC/1xxd
strings $filename > /home/ryan/IS/WOC/2strings
exiftool $filename > /home/ryan/IS/WOC/3exif