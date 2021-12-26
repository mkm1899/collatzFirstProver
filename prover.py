from sympy import *
from binary import Vertex
k = symbols('k')
#expr = 2*k + 2
#x = str(expr)
#print(type(x))
#print(x)
#print(expr)
#expr = (expr)/2
#print(expr)

#Checks if that k is even
def ifEven(expr):
    s = str(expr)
    s = s.replace("k", "(2*k)")
    return parse_expr(s)

#Checks if that k is odd
def ifOdd(expr):
    s = str(expr)
    s = s.replace("k", "(2*k + 1)")
    return parse_expr(s)

#makes sure the expression has to be even
def isEven(expr):
    expr2 = (expr)/2
    s = str(expr2)
    if '/' not in s:
        return expr2
    return None

#makes sure the expression has to be odd
def isOdd(expr):
    expr2 = (expr)-1
    expr2 = (expr2)/2
    s = str(expr2)
    if '/' not in s:
        return expr2
    return None

def createTree(V, depth, endDepth):
    if depth > endDepth:
        return
    change = True
    while(change):
        change = False
        temp = isEven(V.data)
        if temp != None:
            change = True
            V.data = temp
        temp = isOdd(V.data)
        if temp != None:
            #print("When does this run I wonder")
            change=True
            V.data = ((3 * V.data) + 1)/2
    
    if depth != 0:
        if '0' == str(simplify(V.data - V.n)):
            print("Collatz conjecture is false or more likely I made a mistake")
            print(V.data,"\t", V.n)
            return
        if '-' in str(simplify(V.data - V.n)):
            #print(str(simplify(V.data - V.n)))
            #print("It cannot be the first")
            #print(V.data,"\t", V.n)
            return

    if(depth != endDepth-1):
        V.left = Vertex(ifEven(V.data), ifEven(V.n))
        V.right = Vertex(ifOdd(V.data), ifOdd(V.n))
        createTree(V.left, depth+1, endDepth)
        createTree(V.right, depth+1, endDepth)
            

def CreateTree(depth):
    root = Vertex(k, k)
    createTree(root, 0 , depth)
    return root



#root = Vertex(k, k)
#root.print(0)
Maxdepth = 6
r = CreateTree(Maxdepth)
r.printAllTerminatingStuff()
    