# https://adventofcode.com/2022/day/2
file = open ('problem.in', 'r+')
win_dict = {'A':'Y','B':'Z','C':'X'}
lose_dict = {'A':'Z','B':'X','C':'Y'}
def get_score (i):
    if i == 'A' or i == 'X':
        return 1
    elif i == 'B' or i == 'Y':
        return 2
    elif i == 'C' or i == 'Z':
        return 3
_sum = 0
for line in file.readlines():
    line = line[:len(line)-1]
    words = line.split(' ')
    print(words)
    if words[1] == 'Z':
        _sum = _sum + get_score(win_dict[words[0]]) + 6
    elif words[1] == 'Y':
        _sum = _sum + get_score(words[0]) + 3
    else:
        _sum = _sum + get_score(lose_dict[words[0]]) + 0
    print('sum',_sum)
print(_sum)
