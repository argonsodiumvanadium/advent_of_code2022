import os
import math
import sys
from stdlib import *

FNAME = sys.argv[1] if len(sys.argv)>1 else 'input.in'

class Item:
    def __init__ (self,wl):
        self.worry_level=wl
    def __str__ (self):
        return str(self.worry_level)
    
class Monkey:
    def __init__(self,lines):
        self.number=int(lines[0].split(' ')[-1][:-1])
        self.items=[]
        for item in lines[1].split(':')[-1].split(','):
            self.items.append(Item(int(item)))
        self.operation = eval(f"lambda old:{lines[2].split('=')[-1]}")
        self.div=int(lines[3].split(' ')[-1])
        self.test=eval(f"lambda x:x%{lines[3].split(' ')[-1]}==0")
        self.success=int(lines[4].split(' ')[-1])
        self.failure=int(lines[5].split(' ')[-1])
        
def main():
    lines=read_lines(FNAME)
    monkeys=[]
    inspection=[]
    mod=1
    for i in range(8):
        inspection.append(0)
    for i in range(0,len(lines)+1,7):
        monkeys.append(Monkey(lines[i:7+i]))
    for monkey in monkeys:
        mod*=monkey.div
        print('d',mod)
    print('m',mod)

    for i in range(10000):
        print('itru',i)
        monkeys,ins=juggle(monkeys,mod)
        for monkey in monkeys:
            print(*monkey.items)
        inspection=list(map(op('+'),inspection,ins))
    print(inspection.sort())
    print('---')
    print(op("*")(*tuple(inspection[-2:])))
    
def juggle(monkeys,mod):
    print('modu',mod)
    monkeys=monkeys[:]
    inspection=[]
    for j in range(len(monkeys[:])):
        for i in range(len(monkeys[j].items)):
            monkeys[j].items[i].worry_level=(monkeys[j].operation(monkeys[j].items[i].worry_level))
            monkeys[j].items[i].worry_level=monkeys[j].items[i].worry_level%mod
            if monkeys[j].test(monkeys[j].items[i].worry_level):
                monkeys[monkeys[j].success].items.append(monkeys[j].items[i])
            else:
                monkeys[monkeys[j].failure].items.append(monkeys[j].items[i])

        inspection.append(len(monkeys[j].items))
        monkeys[j].items=list([])
    return monkeys,inspection

def read_lines (fname):
    with open(fname) as file:
        return file.read().strip().split('\n')

main()
