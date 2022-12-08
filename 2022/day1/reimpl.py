import os
import math
import sys
from stdlib import *

FNAME='input.in'

def read_lines (fname):
    with open(fname) as file:
        return file.read().split('\n')

# == MAIN ==
a = [0]  
for line in read_lines(FNAME):
    if line:
        a[-1] += int(line)
    else:
        a.append(0)

print(max(a))
