#!/bin/bash
DAY_NO="day$1"

mkdir "$DAY_NO"
cd "$DAY_NO"

touch "${DAY_NO}_1.py"
touch "${DAY_NO}_2.py"
touch "input2.txt"

cat "../template.py" >> "${DAY_NO}_1.py"

INPUT_PATH=""
if [ "$2" = "mac" ]
then
    mv "$HOME/Downloads/input.txt" "input.txt"
else
    mv "/mnt/c/Users/ptdo/Desktop/input.txt" "input.txt"
fi