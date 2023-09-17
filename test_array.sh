#!/bin/bash

declare -a myarray
myarray[0]="trr"
myarray[1]="gytrr"
myarray[2]="trr"
myarray[3]="trr"
myarray[4]="trr"

echo ${myarray[@]}
echo ${#myarray[@]}

for el in ${myarray[@]}
do
	echo $el
done
