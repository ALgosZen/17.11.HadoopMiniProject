#!/bin/bash

for i in {1300..1320}
do
  wget "http://www.gutenberg.org/files/$i/$i.txt"
done
