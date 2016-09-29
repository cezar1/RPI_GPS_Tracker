#!/bin/bash
filename=~/Pictures/$(date +"%Y%m%d_%H%M%S").jpg
raspistill -f -t 2000 -o $filename
