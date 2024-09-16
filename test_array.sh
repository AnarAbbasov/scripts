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


function testfunc()
{
	return 33
}

testfunc xuy

echo $?

echo $@









mystr=5fffbfd
echo $mystr | wc -c
numchars=`echo $mystr | wc -c`
echo ${mystr:3:1}

echo $mystr | cut -c 1-5





for ((i=0;i<9;i=i+1))
{
	echo "tyr"
}

