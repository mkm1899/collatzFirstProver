from sympy import *
# The Node Class defines the structure of a Node
class Vertex:
    # Initialize the attributes of Node
    def __init__(self, data, k):
        self.left = None # Left Child
        self.right = None # Right Child
        self.data = data # Node Data
        self.n = k # what n is equal to at this point
        self.id = -1

    def print(self, depth):
        queue = []
        queue.append((self.left, 1))
        queue.append((self.right, 1))

        overallLength = (2**(depth))# - 2
        tabs = '\t'*(overallLength//2)

        print(tabs, self, end="")
        currentHeight = 0
        while(queue):
            temp = queue.pop(0)
            if(temp[1] >= depth):
                return
            if(temp[1] != currentHeight):
                currentHeight = temp[1]
                tabs = '\t'*(overallLength//(currentHeight*4))
                print()
                #probably needs different spacing for the first of any height which you can do here
            if(temp[0] == None):
                print(tabs, tabs, end="")
                queue.append((None, temp[1]+1))
                queue.append((None, temp[1]+1))
                continue
            queue.append((temp[0].left, temp[1] + 1))
            queue.append((temp[0].right, temp[1] + 1))
            print(tabs, temp[0], tabs, end="")
            
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

    def printAllTerminatingStuff2(self):
        stack = []
        stack.append((self, []))
        print("for all natural numbers n s.t. any of the below are true then if cannot be first") 
        path = []
        while(stack):
            temp = stack.pop()
            path.append(temp[1])
            if temp[0] == None:
                path.pop()
                continue
            s = str(simplify(temp[0].data - temp[0].n))
            if '0' == s and temp[0] != self:
                print("**********************")
                print("Error: unless i proved the collatz conjecture is false")
                print("**********************")
                print(path)
            if '-' in s:
                print("\tn = ", temp[0].n)
                print(path)
            path.pop()
            x = temp[1]
            x.append(False)
            stack.append((temp[0].right, x))
            x = temp[1]
            x.append(True)
            stack.append((temp[0].left, x))
    
    def __str__(self):
        return str(self.n)



