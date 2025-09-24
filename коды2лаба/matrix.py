a=[[1, 2, 3]]
b=[[1], [2], [3]] 
c=[[1, 2], [3, 4]] 
d=[] 
e=[[1, 2], [3]]
def f(x):
    h=[]
    for i in x:
        if isinstance(i,list):
            for k in i:
                h.append([k])
        else:
            h.append([i])
    return h
print(f(a))
print(f(b))
print(f(c))
print(f(d))