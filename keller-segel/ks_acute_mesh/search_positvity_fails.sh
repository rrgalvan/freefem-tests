#!/bin/bash
echo "Searching for positivity broken tests in all .out files under current directory..."
echo "######################################################################################"
for i in `find . -name "*.out"`; do\
	echo ""
	echo "Test file: $i"
	echo "----------------------------------------------------"
	grep "max.u.* Positivity broken" $i -A2 -B4 | head -n7 | grep -v computing; \
done
