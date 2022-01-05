#!/bin/bash
for line in $(<./RoomIdList.csv)
do
    id=`echo $line | awk -F ',' '{print $1}'`
    echo "Start Fetching Room $id Successfully!"
    # echo $id >> Pn.json
    info=$(curl https://api.live.bilibili.com/room/v1/Room/playUrl?cid=$id)
    # echo $info
    echo "{\"roomid\":$id,\"data\":$info}" >> ./data/Pn.json
done
