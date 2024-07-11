#!/bin/bash
mkdir documents/

# Check if a filename is provided as an argument
if [ -z "$1" ]; then
  echo "Usage: $0 filename"
  exit 1
fi

# Open the file and read it line by line
while IFS= read -r line
do
  #echo "-P documents/ $line"
  wget -O documents/$(basename "$line") "$line"
done < "$1"
