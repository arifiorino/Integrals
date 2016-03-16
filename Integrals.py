def LRAM(f, Range, i):
    points=[]
    x=Range[0]
    while x<Range[1]:
        points.append(f(x))
        x+=i
    print(i," * ("+' + '.join([str(point) for point in points])+")=",end=" ")
    print(i*sum(points))
def MRAM(f, Range, i):
    points=[]
    x=Range[0]+(i/2)
    while x<Range[1]:
        points.append(f(x))
        x+=i
    print(i," * ("+' + '.join([str(point) for point in points])+")=",end=" ")
    print(i*sum(points))
def RRAM(f, Range, i):
    points=[]
    x=Range[0]+i
    while x<=Range[1]:
        points.append(f(x))
        x+=i
    print(i," * ("+' + '.join([str(point) for point in points])+")=",end=" ")
    print(i*sum(points))

def TAM(f, Range, i):
    x=Range[0]
    points=[f(x)]
    x+=i
    while x<Range[1]:
        points.append(f(x))
        points.append(f(x))
        x+=i
    points.append(f(x))
    print(".5 *",i," * ("+' + '.join([str(point) for point in points])+")=",end=" ")
    print(.5*i*sum(points))

f=eval("lambda x:"+input("Enter formula: "))
Range=[int(n.strip()) for n in input("Enter Range: ").split(',')]
n=int(input("Enter n: "))
i=(Range[1]-Range[0])/n
TAM(f, Range, i)