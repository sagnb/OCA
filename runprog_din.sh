#!/bin/bash

# 10x10F
for i in $(seq 1 10); do
    python prog_din/main.py generate/10x10F/map$i.txt > generate/10x10F/resultprog_dinmap$i.txt

done

# 10x10M
for i in $(seq 1 10); do
    python prog_din/main.py generate/10x10M/map$i.txt > generate/10x10M/resultprog_dinmap$i.txt

done

# 10x10D
for i in $(seq 1 10); do
    python prog_din/main.py generate/10x10D/map$i.txt > generate/10x10D/resultprog_dinmap$i.txt

done

# 20x20F
for i in $(seq 1 10); do
    python prog_din/main.py generate/20x20F/map$i.txt > generate/20x20F/resultprog_dinmap$i.txt

done

# 20x20M
for i in $(seq 1 10); do
    python prog_din/main.py generate/20x20M/map$i.txt > generate/20x20M/resultprog_dinmap$i.txt

done

# 20x20D
for i in $(seq 1 10); do
    python prog_din/main.py generate/20x20D/map$i.txt > generate/20x20D/resultprog_dinmap$i.txt

done

# 50x50F
for i in $(seq 1 10); do
    python prog_din/main.py generate/50x50F/map$i.txt > generate/50x50F/resultprog_dinmap$i.txt

done

# 50x50M
for i in $(seq 1 10); do
    python prog_din/main.py generate/50x50M/map$i.txt > generate/50x50M/resultprog_dinmap$i.txt

done

# 50x50D
for i in $(seq 1 10); do
    python prog_din/main.py generate/50x50D/map$i.txt > generate/50x50D/resultprog_dinmap$i.txt

done
