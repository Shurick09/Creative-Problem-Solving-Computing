# (1,(7,(6,(),()),(8,(),()),(2,(6),(),()),(3,(5,(),()),(9,(),()))

def leaf(Tree):
    if Tree[1]==() and Tree[2]==():
        return True
    else:
        return False


def sumTree(Tree):
    if leaf(Tree):
        return Tree[0]
    else:
        return Tree[0]+sumTree(Tree[1])+sumTree(Tree[2])

def averageTree(t):
    if leaf(t):
        return t[0]
    else:
        return (sumTree(t)/size(t))

def size(Tree):
    if leaf(Tree):
        return 1
    else:
        return 1 + size(Tree[1]) + size(Tree[2])
    
def mirrorTree(tree):
    if leaf(tree):
        return tree
    else:
        return tree[0],mirrorTree(tree[2]),mirrorTree(tree[1])


