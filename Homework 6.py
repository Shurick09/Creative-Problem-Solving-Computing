def double_strand(s1,s2):
    x='' 
    if len(s1)!=len(s2):
        return False 
    for num in range(0,len(s1)):
        if s1[num]== 'A':
            x=x+'T'
        elif s1[num]=='T':
            x=x+'A'
        elif s1[num]=='C':
            x=x+'G'
        elif s1[num]=='G':
            x=x+'C'
    
    if s2==x:
        return True
    else:
        return False
            
        
        
