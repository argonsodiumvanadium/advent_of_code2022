file = open("matrix.in")
stacks = [[],[],[],[],[],[],[],[],[]]
for line in file.readlines():
    line=line[:-1]
    print(line)
    for i,char in enumerate(line):
        if char == ' ':
            continue
        stacks[i].append(char)

instructions = open("input.in")

def move (stacks, _len, _from, _to ):
    val=stacks[_from].copy()[:_len] + stacks[_to].copy()
    stacks[_from]=stacks[_from].copy()[_len:]
    stacks[_to]=val
    print(stacks)

for line in instructions.readlines():
    instr=line[:-1].split(' ')
    move(stacks,int(instr[1]),int(instr[3])-1,int(instr[5])-1)

print(stacks)
for i in stacks:
    print(i[0])

