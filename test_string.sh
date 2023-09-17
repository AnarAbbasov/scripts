#!/bin/bash

string='testxazx'
len=`echo $string | wc -c`
for (( i=1; i< $len; i++ )) 
do
	echo "character:" $'\t'
	char=`echo  $string | cut  -c$i-$i `
	echo $char $'\t'
done
