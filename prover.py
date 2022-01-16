from sympy import *
from sympy.simplify.fu import L
from binary import Vertex
import pickle
import signal
k = symbols('k')
r = None

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
        return# V, depth
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
            return# None
        if '-' in str(simplify(V.data - V.n)):
            return# None

    if(depth != endDepth-1):
        V.left = Vertex(ifEven(V.data), ifEven(V.n))
        V.right = Vertex(ifOdd(V.data), ifOdd(V.n))
        createTree(V.left, depth+1, endDepth)
        createTree(V.right, depth+1, endDepth)
            

def CreateTree(depth):
    root = Vertex(k, k)
    createTree(root, 0 , depth)
    return root

def saveTree(root):
    with open('tree.pkl', 'wb') as outp:
        pickle.dump(root, outp, pickle.HIGHEST_PROTOCOL)

def loadTree():
    root = None
    try:
        with open('tree.pkl', 'rb') as inp:
            root = pickle.load(inp)
    except FileNotFoundError:
        root = None
    return root


def runFromLoad(root, depth):
    leaves = root.getUnFinishedLeafNodes()
    for x in leaves:
        createTree(x[0], x[1], depth)


def exit_gracefully(signum, frame):
    saveTree(r)
    exit(0)

#-1 depth means infinite
def prove(depth):
    global r
    step = 3
    r = loadTree()
    if r == None:
        if depth <= 16 and depth != -1:
            r = CreateTree(depth)
        else:
            r = CreateTree(16)
    signal.signal(signal.SIGINT, exit_gracefully)
    ndepth = 16 + step
    while(ndepth < depth or depth == -1):
        runFromLoad(r, ndepth)
        ndepth += step
    runFromLoad(r, depth)

    

#-1 equal something special

prove(10)
#saveTree(r)
#r = loadTree()
#r = CreateTree(10)
r.printAllTerminatingStuff()
r.printAllNotFirstFromData()

#r = loadTree()
#if r == None:
#r = CreateTree(Maxdepth)
#r.print("tree16.svg")



#while(True):
#    Maxdepth += 1
#    l = runFromLoad(r, Maxdepth, l)
#r.printAllTerminatingStuff()
#r.print("root12.png")

#saveTree(r)
#r = loadTree()
#runFromLoad(r)

#r.printAllTerminatingStuff()
#r.print("treeFromLoad.png")

#r = CreateTree(10)
#r.print("tree.png")
    