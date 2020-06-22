def replace(x,y,lst):
    if lst==[]:
        return []
    else:
        if lst[0]==x:
           return [y]+replace(x,y,lst[1:])
        else:
            return [lst[0]]+replace(x,y,lst[1:])


def first_n_primes(n,lst):
    return hPrime(n,lst,0)

def hPrime(n,lst,counter):
    if any_prime(lst) == False and len(lst)!=0:
        return "I didn't find any primes."
    while(n!=0):
        if lst==[]:
            return "I only found " + str(counter) + " primes"
        elif is_prime(lst[0])== False:
            return hPrime(n, lst[1:],counter)
        else:
            print lst[0]
            n=n-1
            return hPrime(n,lst[1:],counter+1)
def is_prime(a):
    c=0
    for num in range(2,a):
        if a%num==0:
            c=c+1
    if c==0:
        return True 
    else:
        return False  

def any_prime(myList):
    b=0
    for sym in range(0,len(myList)):
            if is_prime(myList[sym])==True:
                b=b+1
    if b==0:
        return False

def how_many_prime(myList1):
    p=0
    for abc in range(0,len(myList1)):
        if is_prime(myList1[abc])== True:
            p=p+1
    return p  


def findBlack(code, guess, colors):
   return hCount(code,guess,[],colors * [0])

def hCount(code, guess, matches, count):
    if code==[]:
        return [matches,count]
    if code[0]==guess[0]:
        count[code[0]]=count[code[0]]+1
        return hCount(code[1:],guess[1:],matches + ["Black"],count) 
    if code[0]!=guess[0]:
        return hCount(code[1:], guess[1:],matches + ["Dummy"],count)
