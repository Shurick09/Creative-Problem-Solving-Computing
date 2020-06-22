def mismatchedPairs(s1,s2):
    c=0
    if len(s1)!=len(s2):
        return "DNA string don't have same length"
    for num in range(0,len(s1)):
        if s1[num]=='A' and s2[num]!='T':
            c=c+1
        elif s1[num]=='T' and s2[num]!='A':
            c=c+1
        elif s1[num]=='C' and s2[num]!='G':
            c=c+1
        elif s1[num]=='G' and s2[num]!='C':
            c=c+1
    return c

def first_n_primes(n,lst):
    x=0
    c=0
    z=0
    myList=[]
    while z<=n:
        for num in range(2,lst[z]):
            if (lst[z]%num)!=0:
                x=x+1
        if x==lst[z]-2:
             c=c+1
             myList.append(lst[z])
        z=z+1
        x = 0
    if c==0:
        return 'I didnt find any primes'
    elif c==1:
        return 'I only found ' + str(c) + ' prime' + str(myList)
    elif c==n:
        return myList
    else:
        return 'I only found ' + str(c) + ' primes' + str(myList)
            
