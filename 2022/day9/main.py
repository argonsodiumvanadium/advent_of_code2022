import os
import math
import sys
from stdlib import *

FNAME='input.in'

# just call this function with the length of chain (including the head)
def main(l=2):
    mem = {}
    chain = [(0,0)]*l
    for line in read_lines(FNAME):
        if not line: continue
        move,times = line.split(' ')[0],line.split(' ')[1]
        for i in r(int(times)):
            chain = do_move(chain,move)
            mem[chain[-1]] = True
    count=0
    return len(mem)
def do_move(chain, move):
    head=chain[0]
    if move=='R':
        head = (head[0]+1,head[1])
    if move=='L':
        head = (head[0]-1,head[1])
    if move=='U':
        head = (head[0],head[1]+1)
    if move=='D':
        head = (head[0],head[1]-1)
    chain[0]=head

    return move_chain(chain)

def n (num):
    if num:
        if num < 0:
            return -1*num/num
        return num/num
    return num

def move_chain (chain):
    for i in r(len(chain)-1):
        chain[i+1]=dist(chain[i],chain[i+1])
    return chain

def dist (head, tail):
    xdiff = head[0] - tail[0]
    ydiff = head[1] - tail[1]
    if math.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2) > math.sqrt(2):
            return tail[0]+n(xdiff), tail[1]+n(ydiff)
    else:
        return tail
def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')


print("Part 1:",main(2))
print("Part 2:",main(10))
