#!/bin/bash

filename=$(echo $1)

xxd $filename > Text/xxd
strings $filename > Text/strings
exiftool $filename > Text/exif