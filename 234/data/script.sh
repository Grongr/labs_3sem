#!/bin/bash

if [[ $(ls | grep "translated") != "translated" ]]
then
    mkdir translated
fi

for file in $(ls | grep .dat)
do
    python3 translate.py $file
done 

cd translated
