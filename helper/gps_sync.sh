#!/bin/bash
GPSDATE=`gpspipe -w | head -10 | grep TPV | sed -r 's/.*"time":"([^"]*)".*/\1/' | head -1` ; echo $GPSDATE ; sudo date -s "$GPSDATE"

