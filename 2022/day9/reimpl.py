import os
import math
import sys
from stdlib import *

FNAME='input.in'
moves = {
        'R':(1,0),
        'L':(-1,0),
        'U':(0,1),
        'D':(0,-1),
    }

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
    global moves
    chain[0]=chain[0]+moves[move]
    return move_chain(chain)

def move_chain (chain):
    for i in r(len(chain)-1):
        chain[i+1]=dist(chain[i],chain[i+1])
    return chain

def dist (head, tail):
    change=(0,0)
    m=tuple(map(op("-"), head, tail))
    return tail+change

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')


print("Part 1:",main(2))
print("Part 2:",main(10))
