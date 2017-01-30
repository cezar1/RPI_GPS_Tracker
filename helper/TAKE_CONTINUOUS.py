import sys
import time
import os

APP="CAMERA_CONTINUOUS"
while True:
	os.system('bash helper/takePicture2.sh')		
	time.sleep(15)
