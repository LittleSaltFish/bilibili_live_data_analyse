#!/bin/bash
for line in $(ps -aux|grep -v "grep" |grep "python3 ./example.py https://live.bilibili.com/"|awk '{print $2}')
do
    # echo $line
    kill -9 $line
    echo "Successfully Stop AutoFetch : $line"
done

​kill -9 $(ps -aux |grep -v "grep"|grep AutoMessage.sh|awk '{print $2}')
echo "Successfully Stop AutoMessage : $line"

echo "Done!"


