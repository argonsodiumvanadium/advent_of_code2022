import os
import math
import sys

FNAME='input.in'

print("doesnt work for some reason :/")

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

pwd=[]
storage={'/':0}
for line in read_lines(FNAME):
    if not line: continue
    if "$ cd .." in line:
        pwd.pop()
        continue
    if "$ cd /" in line:
        pwd = ['/']
        continue
    elif "$" in line and "cd" in line:
        pwd.append(line.split(' ')[2])
        storage[pwd[-1]] = 0
        continue
    elif "$ ls" in line or "dir " in line:
        continue
    else:
        space=int(line.split(' ')[0])
        for i in pwd:
            storage[i] = int(storage[i]+space)
_sum=[]
for dirname, space in storage.items():
    if space <= 100000:
        _sum.append(space)
print(sum(_sum))

