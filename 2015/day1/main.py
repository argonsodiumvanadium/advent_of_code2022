import os
import math
import sys
from stdlib import *

FNAME='input.in'

def main():
    line=read_lines(FNAME)[0]
    count=0
    for i,char in enumerate([char for char in line]):
        if char == '(':
            count+=1
        else:
            count-=1
        if count < 0:
            print(i+1)
            return
    print(count)

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

main()
