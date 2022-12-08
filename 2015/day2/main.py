import os
import math
import sys
from stdlib import *

FNAME='input.in'

"""
def main():
    areas=[]
    for line in read_lines(FNAME):
        if not line: continue
        print(line)
        dims=ints(line,'x')
        print(dims)
        p=prod(dims)
        elems=[p/dim for dim in dims]
        areas+=[2*sum(elems)+min(elems)]
    
    print(sum(areas))
"""

def main ():
    areas=[]
    for line in read_lines(FNAME):
        if not line:continue
        dims=sorted(ints(line,'x'))
        a=2*sum(dims[:2])
        a+=prod(dims[:])
        areas.append(a)
    print(sum(areas))

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

main()
