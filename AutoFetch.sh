#!/bin/bash
for line in $(</root/Python/bilibili_live_data_analyse/RoomIdList.csv)
do
    id=`echo $line | awk -F',' '{print $1}'`
    echo $id
    python3 /root/Python/bilibili_live_data_analyse/example.py https://live.bilibili.com/$id &
done
