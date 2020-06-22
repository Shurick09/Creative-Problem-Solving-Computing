#1a

def subset(target,L):
    if target==0:
        return True
    elif L==[]:
        return False
    elif L[0]>target:
        return subset(target, L[1:])
    else:
        useIt=subset(target-L[0],L[1:])
        loseIt=subset(target,L[1:])
        return useIt or loseIt

#1b

#Picture

#1c

#subset(15,[10,1,5]) = True

#2a

def LCS(S1,S2):
    if S1=="" or S2=="":
        return 0
    elif S1[0]==S2[0]:
            return 1+LCS(S1[1:],S2[1:])
    else:
        option1=LCS(S1[1:],S2)
        option2=LCS(S1,S2[1:])
        option3=LCS(S1[1:],S2[1:])
        return max(option1,option2,option3)

#2b

#Picture

#2c

#LCS('AAC','ATA')=2

#3a

def ED(S1,S2):
    if S1 == "":
        return len(S2)
    elif S2=="":
        return len(S1)
    elif S1[0]==S2[0]:
        return ED(S1[1:],S2[1:])
    else:
        substitute= 1+ED(S1[1:],S2[1:])
        insert=1+ED(S1,S2[1:])
        delete= 1+ED(S1[1:],S2)
        return min(substitute,insert,delete)

#3b

#Picture

#3c

#ED('soup','sup')= 1

