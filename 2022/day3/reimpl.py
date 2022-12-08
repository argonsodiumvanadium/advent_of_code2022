import os
import math
import sys
from stdlib import *

FNAME='input.in'

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

def evaluate (vals):
    s=0
    for val in vals:
        if val == None:
            continue
        if ord(val) <= ord('Z'):
            s+= ord(val) - ord('A') + 27
        else:
            s+= ord(val) - ord('a') + 1
    return s
# == MAIN ==
vals=[]
for i in range(0,len(read_lines(FNAME)),3):
    line=read_lines(FNAME)[i:i+3]
    print(line)
    if not line[0]: continue
    p1 = line[0]
    p2 = line[1]
    p3 = line[2]
    vals += [(set(p1) & set(p2) & set(p3)).pop() if (set(p1) & set(p2) &set(p3)) else None]
print(evaluate(vals))
