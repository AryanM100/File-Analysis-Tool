#!/bin/bash

filename=$(echo $1)
pass=""

read -sp "Enter Passphrase : " pass

steghide extract -sf $filename -p $pass