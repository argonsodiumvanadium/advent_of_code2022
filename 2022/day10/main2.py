import os
import math
import sys
from stdlib import *

FNAME = sys.argv[1] if len(sys.argv)>1 else 'tinput.in'

def main():
    instructions=[]
    cycles=0
    sig=0
    val=0
    inproc=False
    lines=read_lines(FNAME)
    i=0
    X = 1
    lval=0
    arr=[0,1,2]
    while True:
        if not (cycles)%40:
            print('')
            sig += cycles*(X-lval)
        if not inproc:
            lval=0
            if i >= len(lines):
                break
            if 'addx' in lines[i]:
                val=int(lines[i].split(' ')[-1])
                inproc=True
            i=i+1
            arr=draw(cycles,arr)
        else:
            arr=draw(cycles,arr)
            lval=val
            X+=val
            arr=[X-1,X,X+1]
            val=0
            inproc=False
        cycles+=1

 
    print(sig)

def draw(cycles,pts):
#   print('cycles',cycles,'pts',pts)
    cycles=cycles%40
    if not len(pts): 
        print('.',end='')
        return pts
    if cycles in pts:
        print('#',end='')
        return pts[1:]
    else:
        print('.',end='')
        return pts

def read_lines (fname):
    with open(fname) as file:
        return file.read().strip().split('\n')

main()
