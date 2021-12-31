#!bin/bash
time=$(date "+%Y-%m-%d_%H:%M:%S")
echo $time
zip -r $time.zip $(ls test)
