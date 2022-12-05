# https://adventofcode.com/2022/day/1
file = open('aoc1.in')
elves = []
_sum=0
lines = file.readlines()
print(lines)
for line in lines:
    line=line.replace('\n','')
    print(line)
    if line:
        _sum=_sum+int(line)
    else:
        elves.append(_sum)
        _sum=0

elves.append(_sum)
elves.sort(reverse=True)
print(sum(elves[0:3]))
print(elves.index(max(elves)))
print(len(elves))

