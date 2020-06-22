D={}


def salaryUpdate(l):
    return hSalaryUpdate(l,[[[0] for x in range(len(l))] for y in range(len(l))],0)

def hSalaryUpdate(oList,fList,counter):
    if oList==[]:
        return fList
    else:
        fList[counter][0]=oList[0][0]
        fList[counter][1]=float(oList[0][1]) * 1.02
        counter=counter+1
        return hSalaryUpdate(oList[1:],fList, counter)


def path(x,y,l):
    if x==y:
        return True
    elif l==[]:
        return False
    elif x!=l[0][0]:
        return path(x,y,l[1:])
    else:
        useIt= path(l[0][1],y,l[1:])
        loseIt=path(x,y,l[1:])
        return useIt or loseIt


def mSubset(target,numberList):
    if target == 0:
        return True
    elif numberList == ():
        return False
    elif (target,numberList) in D:
        return D[(target,numberList)]
    elif numberList[0] > target:
        return mSubset(target, numberList[1:])
    else:
        useIt = mSubset(target - numberList[0], numberList[1:])
        loseIt = mSubset(target, numberList[1:])
        optimal= useIt or loseIt
        D[(target,numberList)]=optimal
        return optimal
    
    
