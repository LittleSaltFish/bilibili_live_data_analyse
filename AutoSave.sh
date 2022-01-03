#!bin/bash
time=$(date "+%Y-%m-%d_%H:%M:%S")
echo $time
zip -r ./data/FetchHistory/$time.zip ./data/Rooms/* ./data/OutPut/*

rm -r ./data/OutPut/*
rm ./data/Rooms/*

echo "Clean Up Successfully"
