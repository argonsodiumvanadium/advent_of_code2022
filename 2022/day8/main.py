import os
import math
import sys
from stdlib import *

FNAME='input.in'

def main():
    _map=[]
    for line in read_lines(FNAME):
        if not line: continue
        trees = inti([char for char in line])
        _map.append(trees[:])

    checkvisibletrees(_map)

def checkvisibletrees(trees):
    count=2*len(trees[0]) + 2*(len(trees)-2)
    print(count)
    for x in range(1,len(trees)-1):
        for y in range(1,len(trees[x])-1):
            if checkvisibilityx(trees,x,y) or checkvisibilityy(trees,x,y):
                print(x,y)
                count+=1
    print(count)

def checkvisibilityx(trees,x,y):
    vis1=True
    for xi in range(0, x):
        if trees[xi][y] >= trees[x][y]:
            vis1=False
    vis2=True
    for xi in range(x+1,len(trees)):
        if trees[xi][y] >= trees[x][y]:
            vis2=False
    return vis2 or vis1

def checkvisibilityy(trees,x,y):
    vis1=True
    for yi in range(0, y):
        if trees[x][yi] >= trees[x][y]:
            vis1=False
    vis2=True
    for yi in range(y+1,len(trees[x])):
        if trees[x][yi] >= trees[x][y]:
            vis2=False
    return vis2 or vis1

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

main()
