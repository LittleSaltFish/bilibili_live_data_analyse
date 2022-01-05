#!bin/bash
time=$(date "+%Y-%m-%d_%H:%M:%S")
echo $time
zip -r ./data/FetchHistory/$time.zip ./data/Rooms/* ./data/OutPut/* ./data/Pn.json ./data/Info.json

rm -r ./data/OutPut/*
rm ./data/Rooms/*
rm ./data/Pn.json ./data/Info.json

echo "Clean Up Successfully"
