import math
"""
data  : string to be converted to ints
delim :
    - if None : delimits on whitespace characters " ","\n","\r" etc
    - if 0    : delimits on every character ["a","b","c"] for string "abc"
    - else    : uses passed delimiter
"""
def ints(data:str,delim=None):
    if delim == 0:
        return inti([char for char in data])
    return inti(data.split(delim))

"""
returns a list of items with int items
"""
def inti(items:list):
    return [int(elem) for elem in items]

"""
returns function doing said operation
"""
def op(operation):
    return eval(f"lambda x,y : x {operation} y")

"""
basicall map lmfao
"""
def foreach (items, func):
    return [func(item) for item in items]

"""
basically generic function over a list
"""
def fcat (items,initial,func):
    cat=initial

    for item in items:
        cat=func(cat,item)
    return cat

"""
mutates (arr) to (arr[:i] + arr[j:])
returns          (arr[i:j]          )
"""
def cut(arr:list,i:int,j:int):
    ret = arr[i:j]
    for i in range(i,j):
        del arr[i]
    return ret

"""
returns row of a matrix
"""
def row (arr,i):
    return arr[i]

"""
returns column of a matrix
"""
def col (arr,i):
    return [elem[i] for elem in arr]

"""
returns product of all elemeents in an array
"""
def prod(arr):
    return fcat(arr,1,op('*'))

"""
shorthand range
"""
def r(start,end=None,step=1):
    if not end:
        return range(0,start,step)
    else:
        return range(start,end,step)
"""
pythagoras theorum
"""
def pyth(a,b):
    return math.sqrt(a**2 + b**2)
