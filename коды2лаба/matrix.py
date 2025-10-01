a=[[1, 2, 3]]
b=[[1], [2], [3]] 
c=[[1, 2], [3, 4]] 
d=[] 
e=[[1, 2], [3]]
def f1(x):
    h=[]
    for i in x:
        if isinstance(i,list):
            for k in i:
                h.append([k])
        else:
            h.append([i])
        return h
def f2(x):
    h=[]
    for i in x:
        for j in i:
            h.append(j)
    return h
def f3(x):
    y=[x[0][0], x[1][0]]
    z=[x[0][1], x[1][1]]
    return [y,z]
def f4(x):
    for i in range(len(x)-1):
        if len(x[i])!=len(x[i+1]):
            print("ValueError")
print(f1(a))
print(f2(b))
print(f3(c))
print(f2(d))
print(f4(e))


test1=[[1, 2, 3], [4, 5, 6]] 
test2=[[-1, 1], [10, -10]] 
test3=[[0, 0], [0, 0]] 
test4=[[1, 2], [3]]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(mat)-1):
        if len(mat[i])!=len(mat[i+1]):
            print("ValueError")
        else:
            return [sum(mat[i]),sum(mat[i+1])]
print(row_sums(test1))
print(row_sums(test2))
print(row_sums(test3))
print(row_sums(test4))      

test1=[[1, 2, 3], [4, 5, 6]]
test2=[[-1, 1], [10, -10]] 
test3=[[0, 0], [0, 0]] 
test4=[[1, 2], [3]]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    for enum1 in range(len(mat)-1):
        if len(mat[enum1])!=len(mat[enum1+1]):
            print("ValueError")
        else:
            list1 = []
            for enum2 in zip(*mat): 
                list1.append(sum(enum2))
    return list1
print(col_sums(test1))
print(col_sums(test2))
print(col_sums(test3))
print(col_sums(test4))