#!/bin/bash
for line in $(ps -aux|grep -v "grep" |grep "python3 ./example.py https://live.bilibili.com/"|awk '{print $2}')
do
    # echo $line
    kill -9 $line
    echo "Successfully Stop $line"
done

echo "Done!"

# ps -aux|grep example.py|awk '{print $2}'

