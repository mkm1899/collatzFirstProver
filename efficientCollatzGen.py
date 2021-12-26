f = open("equations.txt", "r")
Start = 3


def initForBody():
    return [0]

def addCol(oldIncBy, forBody):
    for i in range(len(forBody)):
        x = forBody[i]
        forBody.append(x + oldIncBy)
    return forBody

def breakEquation(equation):
    temp = equation.find("*k")
    knum = int(equation[0:temp])
    temp = equation.find("+")
    cnum = 0
    if temp != -1:
        cnum = int(equation[temp+2:])
    return knum, cnum

def remCol(forbody, equation):
    knum, cnum = breakEquation(equation)
    for i in range(len(forbody)-1, -1, -1):
        if ((forbody[i] + Start) - cnum)%knum == 0:
            forbody.pop(i)
    return forbody


forBody = initForBody()
incBy = 1
for x in f:
    if x[0] == '\t':
        eq = x[6:-1]
        knum, _  = breakEquation(eq)
        while(knum > incBy):
            forBody = addCol(incBy, forBody)
            incBy *= 2
        remCol(forBody, eq)

#NOW WRITES THE CODE
f.close()
f = open("header.txt", "r")
f2 = open("collatz3.c", "w")
f2.write(f.read())
f.close()
x = "\tfor(int i = " + str(Start) + "; i < end; i+=" + str(incBy)+ "){\n"
for b in forBody:
    x += "\t\tcheck(i+" + str(b) +");\n"
x += "\t}\n}\n\n"
f2.write(x)

f = open("footer.txt", "r")
f2.write(f.read())
f.close()
f2.close()