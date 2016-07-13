#!/bin/bash
SESSION=$USER

tmux has-session -t $SESSION 2>/dev/null

if [ "$?" -eq 1 ] ; then

tmux -2 new-session -d -s $SESSION

# Setup a window for tailing log files
tmux new-window -t $SESSION:1 -n 'Pressure/Temp'
tmux send-keys "cd ~/repos/Adafruit_Python_BMP/examples" C-m
tmux send-keys "watch -n 2 sudo python simpletest.py" C-m

tmux new-window -t $SESSION:2 -n 'Accelerometer'
tmux send-keys "cd ~/repos/Adafruit_Python_BNO055/examples" C-m
tmux send-keys "sudo python simpletest.py" C-m

tmux new-window -t $SESSION:3 -n 'GPS'
tmux send-keys "sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock" C-m
tmux send-keys "cgps -s" C-m

tmux new-window -t $SESSION:4 -n 'Uptime'
tmux split-window -h
tmux select-pane -t 0
tmux send-keys "while [[ 1 ]]; do uptime >> uptime.log;sleep 10; done" C-m
tmux select-pane -t 1
tmux send-keys "tail -f uptime.log" C-m

tmux new-window -t $SESSION:5 -n 'Camera'
tmux split-window -h
tmux select-pane -t 0
tmux send-keys "cd ~/stills" C-m
tmux send-keys "./../repos/RPI_GPS_Tracker/helper/takePicture.sh" C-m
tmux select-pane -t 1
tmux send-keys "cd ~/stills" C-m
tmux send-keys "watch -n 10 du -h" C-m

tmux new-window -t $SESSION:6 -n 'LEDs'
tmux send-keys "cd helper" C-m
tmux send-keys "./switchLEDs.sh" C-m

tmux new-window -t $SESSION:7 -n 'SCREEN'
tmux send-keys "cd helper" C-m
tmux send-keys "python SCREEN_LISTENER_GPIO.py 23" C-m

# Set default window
tmux select-window -t $SESSION:0
tmux send-keys "top" C-m

fi
# Attach to session

tmux -u -2 attach-session -t $SESSION
