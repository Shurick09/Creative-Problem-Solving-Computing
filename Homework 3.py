#Alex Rozenblit
#09/16/2016
#I pledge my honor that I have abided by the Stevens Honor System.

def min_list(x):
    return min(x)

def gauss(N):
    listX = range(N+1)
    return sum(listX)

def sumOfSquares(N):
    listY= range(N+1)
    listZ = map(square, listY)
    return sum(listZ)


def square(N):
    return N** 2
