def ints(data:str,delim=None):
    if delim:
        return inti(data.split(delim))
    return inti(data.split())

def inti(items:list):
    return [int(elem) for elem in items]

def oper(operation):
    return eval(f"lambda x,y : x {operation} y")

"""
mutates (arr) to (arr[:i] + arr[j:])
returns          (arr[i:j]          )
"""
def cut(arr:list,i:int,j:int):
    ret = arr[i:j]
    for i in range(i,j):
        del arr[i]
    return ret

def row (arr,i):
    return arr[i]

def col (arr,i):
    return [elem[i] for elem in arr]

def prod(arr):
    p=arr[0]
    for i in arr[1:]:
        p*=i
    return p
