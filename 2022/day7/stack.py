import os
import math
import sys

FNAME='input.in'

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
        storage['/'.join(pwd)] = 0
        continue
    elif "$ ls" in line or "dir " in line:
        continue
    else:
        space=int(line.split(' ')[0])
        for i in range(1,len(pwd)+1):
            key='/'.join(pwd[:i])
            storage[key] = storage[key] + space
_sum=[]
for dirname, space in storage.items():
    if space <= 100000:
        _sum.append(space)
print('part 1',sum(_sum))
potential_dirs=[]
for dirname, space in storage.items():
    if space >= (30000000 - (70000000 - storage['/'])):
        potential_dirs.append(space)
print('part 2',min(potential_dirs))

