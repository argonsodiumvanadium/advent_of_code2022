line=input()

seen=[]
for i,char in enumerate(line):
    if len(seen) == 14:
        print(i)
    if char in seen:
        seen=seen[seen.index(char)+1:]
    seen.append(char)
