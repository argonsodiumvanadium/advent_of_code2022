from stdlib import *
import numpy as np

from string import punctuation

def main (lines):
    nums = []
    e_score = []
    def nearby(x,y):
        return [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1)]
    def get_num_at(lines, x, y, idx_done):
        if (x,y) in idx_done:
            return idx_done, 0
        nstr = lines[x][y]
        for yn,i in list(enumerate(lines[x]))[:y][::-1]:
            if (x,yn) in idx_done:
                return idx_done,0
            if i in "0123456789":
                idx_done.add((x,yn))
                nstr += i
            else:
                break
        nstr = nstr[::-1]
        for yn,i in list(enumerate(lines[x]))[y+1:]:
            if (x,yn) in idx_done:
                return idx_done,0
            if i in "0123456789":
                idx_done.add((x,yn))
                nstr += i
            else:
                break
        
        return idx_done,int(nstr)

    idx_done = set()
    gears = []
    for i,l in enumerate(lines):
        if not l: continue
        for j,char in enumerate(l):
            gear = False
            num_gears = []
            if char in punctuation.replace(".",""):
                x,y = i,j
                gear = char == "*"
                npts = nearby(x,y)
                for x,y in npts:
                    x,y = np.clip(x,0,len(lines)), np.clip(y,0,len(l))
                    if lines[x][y] in "0123456789":
                        idx_done,n = get_num_at(lines,x,y,idx_done)
                        num_gears.append(n)
                        nums.append(n)
                num_gears = [n for n in num_gears if n != 0]
                if len(num_gears) == 2 and gear:
                    e_score.append(num_gears[0]*num_gears[1])
    return sum(e_score)

if __name__ == "__main__":
    lines = open("in.txt").read().splitlines()
    print(main(lines))
