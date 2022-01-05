#!/bin/bash
for line in $(ps -aux|grep -v "grep" |grep "python3 ./example.py https://live.bilibili.com/"|awk '{print $2}')
do
    echo $line
    kill -9 $line
    echo "Successfully Stop AutoFetch : $line"
done

for line in $(ps -aux |grep -v "grep"|grep "AutoMessage.sh"|awk '{print $2}')
do
    kill -9 $line
    echo "Successfully Stop AutoMessage : $line"
done

echo "Done!"


