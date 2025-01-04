#!/bin/bash

filename=$(echo $1)
pass=""

read -p "Enter Passphrase : " pass

steghide extract -sf $filename -p $pass