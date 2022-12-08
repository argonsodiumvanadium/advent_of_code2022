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
    counts=[]
    for x in range(1,len(trees)-1):
        for y in range(1,len(trees[x])-1):
            prod=checkvisibilityx(trees,x,y) * checkvisibilityy(trees,x,y)
            print(prod)
            counts.append(prod)
    print(max(counts))

def checkvisibilityx(trees,x,y):
    vis1=True
    score=0
    print('tree',trees[x][y])
    for xi in range(0, x)[::-1]:
        if trees[xi][y] >= trees[x][y]:
            score=abs(xi-x)
            break
    if score == 0:
        score=x
    print('score',score)
    score2=0
    for xi in range(x+1,len(trees)):
        if trees[xi][y] >= trees[x][y]:
            score2=abs(xi-x)
            break
    if score2 == 0:
        score2=len(trees)-x-1
    print('score2',score2)
    return score*score2

def checkvisibilityy(trees,x,y):
    score=0
    for yi in range(0, y)[::-1]:
        if trees[x][yi] >= trees[x][y]:
            score=abs(yi-y)
            break
    if score == 0:
        score=y
    score2=0
    print('yscore',score)
    for yi in range(y+1,len(trees[x])):
        if trees[x][yi] >= trees[x][y]:
            score2=abs(yi-y)
            break
    if score2 == 0:
        score2=len(trees[x])-y-1
    print('score2',score2)
    return score*score2
def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

main()
