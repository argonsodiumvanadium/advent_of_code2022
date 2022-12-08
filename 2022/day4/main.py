file = open("input.in")

_sum = 0

def compare (arg):
    mem = []
    mem.append(sorted([int(numeric_string) for numeric_string in arg[0].split('-')]))
    mem.append(sorted([int(numeric_string) for numeric_string in arg[1].split('-')]))
    mem=sorted(mem)
    if mem[0][1] >= mem[1][0]: 
        print(mem)
        return True
#    if mem[1][0] <= mem[0][0] and mem[1][1] >= mem[0][1]:
 #       return False #True
for line in file.readlines():
    assignments = line[:-1].split(',')
    if compare(assignments):
        _sum = _sum + 1
print(_sum)
