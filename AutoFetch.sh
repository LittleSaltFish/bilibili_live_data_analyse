#!/bin/bash
for line in $(<./RoomIdList.csv)
do
    id=`echo $line | awk -F ',' '{print $1}'`
    echo "Start Fetching Room $id Successfully!"
    python3 ./example.py https://live.bilibili.com/$id &
done
