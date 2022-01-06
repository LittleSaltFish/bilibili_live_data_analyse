#!bin/bash
time=$(date "+%Y-%m-%d_%H:%M:%S")
echo $time
zip -r ./data/FetchHistory/$time.zip ./data/Rooms/* ./data/OutPut/* ./data/Useful/* ./data/Pn.json ./data/PnOut.csv ./data/Info.json ./data/Info.csv

rm -r ./data/OutPut/*
rm -r ./data/Useful/*
rm ./data/Rooms/*
rm ./data/Pn.json ./data/Info.json ./data/PnOut.csv ./data/Info.csv

echo "Clean Up Successfully"
