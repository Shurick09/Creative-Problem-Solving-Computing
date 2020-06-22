def replace(x,y,lst):
    def swap(z):
        if z==x:
            return y
        else:
            return z
    return map(swap,lst)


def replace1(a,b,lst1):
    newList=list()
    for num in range(0,len(lst1)):
        if lst1[num]==a:
            newList.append(b)
        else:
            newList.append(lst1[num])
    return newList
    

def x_count(w,myList):
    if myList==[]:
        return 0
    def check(r):
        if r==w:
            return 1
        else:
            return 0
    def add(c,d):
        return c+d
    return reduce(add,map(check,myList))


def x_count1(t,myList1):
    if myList1==[]:
        return 0
    g=0
    for sym in range(0,len(myList1)):
        if myList1[sym]==t:
            g=g+1
    return g


# mystery(3)
# 3%2=!0
# return true
