#!/bin/bash

# 10x10F
for i in $(seq 1 10); do
    python kohonen/main.py generate/10x10F/map$i.txt > generate/10x10F/resultmap$i.txt

done

# 10x10M
for i in $(seq 1 10); do
    python kohonen/main.py generate/10x10M/map$i.txt > generate/10x10M/resultmap$i.txt

done

# 10x10D
for i in $(seq 1 10); do
    python kohonen/main.py generate/10x10D/map$i.txt > generate/10x10D/resultmap$i.txt

done

# 20x20F
for i in $(seq 1 10); do
    python kohonen/main.py generate/20x20F/map$i.txt > generate/20x20F/resultmap$i.txt

done

# 20x20M
for i in $(seq 1 10); do
    python kohonen/main.py generate/20x20M/map$i.txt > generate/20x20M/resultmap$i.txt

done

# 20x20D
for i in $(seq 1 10); do
    python kohonen/main.py generate/20x20D/map$i.txt > generate/20x20D/resultmap$i.txt

done

# 50x50F
for i in $(seq 1 10); do
    python kohonen/main.py generate/50x50F/map$i.txt > generate/50x50F/resultmap$i.txt

done

# 50x50M
for i in $(seq 1 10); do
    python kohonen/main.py generate/50x50M/map$i.txt > generate/50x50M/resultmap$i.txt

done

# 50x50D
for i in $(seq 1 10); do
    python kohonen/main.py generate/50x50D/map$i.txt > generate/50x50D/resultmap$i.txt

done
