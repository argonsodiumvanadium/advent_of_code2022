def ints(data:str,delim=None):
    if delim:
        return inti(data.split(delim))
    return inti(data.split())

def inti(items:list):
    return [int(elem) for elem in items]

def oper(operation):
    return eval(f"lambda x,y : x {operation} y")
