while [ true ]; do
filename=$(date -u +"%d%m%Y_%H%M-%S").jpg
raspistill -o $filename
sleep 5;
find * -mmin +$((3)) -type f -exec rm {} \;
done;
