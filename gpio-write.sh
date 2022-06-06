#!/bin/bash

source gpio-cmd.sh

echo "WRITE $2 TO GPIO$1"
writeGPIO $1 $2
