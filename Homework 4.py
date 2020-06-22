def head(x):
    if len(x)==0:
        return 'Error: The empty list has no head'
    else:
        return x[0]

def tail(lst):
    if len(lst)==0:
        return 'Error: The empty list has no tail'
    else:
        return lst[1:]



def replace_and_triple(x,y,z,lst1):
    if z==x:
       return lst1
    elif lst1==[]:
        return []
    def swap(d):
        if d==x:
            return y
        elif d==z:
            return d*3
        else:
            return d
        
    lst2=map(swap,lst1)
    return lst2
