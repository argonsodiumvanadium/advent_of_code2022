from stdlib import *

def main (lines):
    ans = []
    l = ["zero","one", "two", "three", "four", "five", "six", "seven" , "eight", "nine" ]
    itd = tuple(zip(l,foreach(range(10),str)))
    for line in lines:
        num = ""
        start = True
        end = ""
        nl = ""
        print(line)
        for i in range(len(line)):
            for sn,n in itd:
                if line[i:].startswith(sn):
                    nl += n
                    break
                if line[i] in "0123456789":
                    nl += line[i]
                    break
        line = nl
        print(line)
        for char in line:
            if char in "0123456789" and start :
                num = char
                start = False
            if char in "0123456789":
                end = char
        print(num+end)
        ans.append(int(num + end))
    return sum(ans)

if __name__ == "__main__":
    lines = open("in.txt").read().splitlines()
    print(main(lines))
