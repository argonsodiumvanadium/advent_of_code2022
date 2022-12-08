import os
import math
import sys
from stdlib import *

FNAME='input.in'

def main():
    count=0
    for line in read_lines(FNAME):
        if not line: continue
        words=line.split(',')
        print(line,words)
        s1=set(range(*(ints(words[0],'-')+[ints(words[0],'-')[-1]])))
        s2=set(range(*(ints(words[1],'-')+[ints(words[1],'-')[-1]])))


        sc = s1|s2
        if len(sc) == len(s1) or len(s2) == len(sc):
            count+=1
    print(count)

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

main()
