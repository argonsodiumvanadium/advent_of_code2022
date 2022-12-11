import os
import math
import sys
from stdlib import *

FNAME = sys.argv[1] if len(sys.argv)>1 else 'input.in'

def main():
    for line in read_lines(FNAME):
        if not line: continue

def read_lines (fname):
    with open(fname) as file:
        return file.read().strip().split('\n')

main()
