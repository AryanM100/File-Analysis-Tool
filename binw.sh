#!/bin/bash

filename=$(echo $1)

echo -e "\nBinwalk -"

binwalk -B $filename | awk 'NF {print $0}' | tee "/home/ryan/IS/WOC/4binw"

read -p "Extract using Binwalk ?"$'\n' a

if [[ "$a" == "Y" || "$a" == "y" || "$a" == "yes" || "$a" == "Yes" || "$a" == "YES" ]]; then
    binwalk --dd=".*" $filename > "/home/ryan/IS/WOC/4binw"
fi