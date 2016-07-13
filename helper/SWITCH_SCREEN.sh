#!/bin/bash
if [ $# -eq 1 ]; then
	if [ "$1" -eq "1" ]; then
		echo "Switching screen ON"
		sudo  ~/repos/hub-ctrl.c/hub-ctrl -h 0 -P 2 -p 1
#		sudo  ~/repos/hub-ctrl.c/hub-ctrl -b 001 -d 029 -p 1
	elif [ "$1" -eq "0" ]; then
		echo "Switching screen OFF"
		sudo  ~/repos/hub-ctrl.c/hub-ctrl -h 0 -P 2 -p 0
#		sudo  ~/repos/hub-ctrl.c/hub-ctrl -b 001 -d 029 -p 0
	else
		echo "Unknown option!"
	fi
else
	echo "Usage <script> [0/1]";
fi
