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
    while True:
        if not (cycles-20)%40:
            print('no',cycles,X-lval)
            sig += cycles*(X-lval)
        
        if not inproc:
            lval=0
            if i >= len(lines):
                break
            if 'addx' in lines[i]:
                val=int(lines[i].split(' ')[-1])
                inproc=True
            i=i+1
        else:
            lval=val
            X+=val
            val=0
            inproc=False
        cycles+=1

 
    print(sig)


def read_lines (fname):
    with open(fname) as file:
        return file.read().strip().split('\n')

main()
