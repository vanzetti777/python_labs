# a=[[1, 2, 3]]
# b=[[1], [2], [3]] 
# c=[[1, 2], [3, 4]] 
# d=[] 
# e=[[1, 2], [3]]
# def f1(x):
#     h=[]
#     for i in x:
#         if isinstance(i,list):
#             for k in i:
#                 h.append([k])
#         else:
#             h.append([i])
#         return h
# def f2(x):
#     h=[]
#     for i in x:
#         for j in i:
#             h.append(j)
#     return h
# def f3(x):
#     y=[x[0][0], x[1][0]]
#     z=[x[0][1], x[1][1]]
#     return [y,z]
# def f4(x):
#     for i in range(len(x)-1):
#         if len(x[i])!=len(x[i+1]):
#             print("ValueError")
# print(f1(a))
# print(f2(b))
# print(f3(c))
# print(f2(d))
# print(f4(e))


# a=[[1, 2, 3], [4, 5, 6]] 
# b=[[-1, 1], [10, -10]] 
# c=[[0, 0], [0, 0]] 
# d=[[1, 2], [3]]
# def f(x):
#     for i in range(len(x)-1):
#         if len(x[i])!=len(x[i+1]):
#             print("ValueError")
#         else:
#             return [sum(x[i]),sum(x[i+1])]
# print(f(a))
# print(f(b))
# print(f(c))
# print(f(d))      

a=[[1, 2, 3], [4, 5, 6]]
b=[[-1, 1], [10, -10]] 
c=[[0, 0], [0, 0]] 
d=[[1, 2], [3]]
def f(x):
    for i in range(len(x)-1):
        if len(x[i])!=len(x[i+1]):
            print("ValueError")
        else:
            h = []
            for j in zip(*x): 
                h.append(sum(j))
    return h
print(f(a))
print(f(b))
print(f(c))
print(f(d))