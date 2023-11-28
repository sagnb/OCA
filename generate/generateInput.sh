#!/bin/bash

# 10x10F
for i in $(seq 1 100); do
    printf "10\n10\nF\nQ\n10x10F/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 10x10M
for i in $(seq 1 100); do
    printf "10\n10\nM\nQ\n10x10M/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 10x10D
for i in $(seq 1 100); do
    printf "10\n10\nD\nQ\n10x10D/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 20x20F
for i in $(seq 1 100); do
    printf "20\n20\nF\nQ\n20x20F/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 20x20M
for i in $(seq 1 100); do
    printf "20\n20\nM\nQ\n20x20M/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 20x20D
for i in $(seq 1 100); do
    printf "20\n20\nD\nQ\n20x20D/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 50x50F
for i in $(seq 1 100); do
    printf "50\n50\nF\nQ\n50x50F/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 50x50M
for i in $(seq 1 100); do
    printf "50\n50\nM\nQ\n50x50M/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done

# 50x50D
for i in $(seq 1 100); do
    printf "50\n50\nD\nQ\n50x50D/map$i.txt" > input.txt
    python generateLevelObstacleFinalTest.py < input.txt
done
