from sympy import *
import graphviz
from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import bisect

#from efficientCollatzGen import breakEquation
# The Node Class defines the structure of a Node

def breakEquation(equation):
        temp = equation.find("*k")
        knum = int(equation[0:temp])
        temp = equation.find("+")
        cnum = 0
        if temp != -1:
            cnum = int(equation[temp+2:])
        return knum, cnum

# since 1162261467 is 3^39 the largest power of 3 that fits in a 64 bit int you can quickly deduce it is a power of 3
def isPowerOfThree(n):
    return (n > 0 and 4052555153018976267 % n == 0)

class Vertex:
    # Initialize the attributes of Node
    def __init__(self, data, k):
        self.left = None # Left Child
        self.right = None # Right Child
        self.data = data # Node Data
        self.n = k # what n is equal to at this point
        self.id = -1
    
    #when looking at the graph generated the top equation is what n was made equal to
        #the bottom equation is after all the iterations of the collatz conjecture on n (that you can do with absolute certainty)
    #the left branch is if k is even and the right branch is if the k is odd
    def print(self, filename):
        queue = []

        root = Node(str(self))
        queue.append((self.left, root))
        queue.append((self.right, root))
        
        while(queue):
            temp = queue.pop(0)
            if(temp[0] == None):
                continue
            parent = temp[1]
            cur = Node(str(temp[0]), parent=parent)
            queue.append((temp[0].left, cur))
            queue.append((temp[0].right, cur))

        DotExporter(root).to_picture(filename)
    
    

    #gets unfinishedLeafNodes
    def getUnFinishedLeafNodes(self):
        leafNodes = []
        queue = []
        queue.append((self,0))
        while(queue):
            temp = queue.pop(0)
            if temp[0].left != None:
                #since nodes either have two or 0 leaf nodes this is alright
                queue.append((temp[0].left, temp[1]+1))
                queue.append((temp[0].right, temp[1]+1))
            else:
                if '-' not in str(simplify(temp[0].data - temp[0].n)):
                    leafNodes.append(temp)
        return leafNodes
            
    #just the power of two stuff which were proven by showing that those set of numbers have to be generated by a smaller number
    def printAllTerminatingStuff(self):
        queue = []
        queue.append(self)
        print("for all natural numbers n s.t. any of the below are true then if cannot be first") 
        while(queue):
            temp = queue.pop(0)
            if temp == None:
                continue
            s = str(simplify(temp.data - temp.n))
            if '0' == s and temp != self:
                print("**********************")
                print("Error: unless i proved the collatz conjecture is false")
                print("**********************")
            if '-' in s:
                print("\tn = ", temp.n)
            queue.append(temp.left)
            queue.append(temp.right)

    #returns false if it is already covered by a different equation
    #returns true otherwise
    def __checkForRepeats(self, list, equation):
        mk,mc = breakEquation(str(equation))
        for x in list:
            tk, tc = x
            #since mk and tk should always be powers of 3 doing > instead of mod should suffice
            if(mk%tk == 0):
                if ((mc-tc)%tk == 0):
                    return False
        return True





    def printAllNotFirstFromData(self):
        list = []
        queue = []
        queue.append(self.left)
        queue.append(self.right)
        print("for all natural numbers n s.t. any of the below are true then if cannot be first") 
        while(queue):
            temp = queue.pop(0)
            if temp == None:
                continue
            s = str(simplify(temp.data - temp.n))
            if '0' == s and temp != self:
                print("**********************")
                print("Error: unless i proved the collatz conjecture is false")
                print("**********************")
            elif '-' not in s:
                # this is proven because a smaller number can be turned into data. 
                    # For example: all n = 3k+2 is true because if n = (3k + 1)/2 and k is odd: that means you dont have to prove n because k is smaller and therefore "theoretically" proven
                        #another way to look at: n cant be first because if there exsists a valid looped or infinite sequence, then there cannot be a viable sequence with a smaller number or that smaller number would have been first.
                            #This is more obvious when you look at a generated graph and look at the first two comments on the print function above
                if(self.__checkForRepeats(list, temp.data)):
                    print("\tn = ", temp.data)
                    t = breakEquation(str(temp.data))
                    #bisect.insort(list, t)
                    list.append(t)

            queue.append(temp.left)
            queue.append(temp.right)
    
    def __str__(self):
        return str(self.n)+"\n"+str(self.data)



