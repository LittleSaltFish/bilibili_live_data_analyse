#!/bin/bash
for line in $(<./test/SampleId.csv)
do
    id=$(echo $line | awk -F ',' '{print $1}')
    echo $id
done
