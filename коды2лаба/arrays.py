# s=list(input().split())
# s1=[]
# for i in s:
#     if '.' in i:
#         s1.append(float(i))
#     else:
#         s1.append(int(i))

# if len(s1)==0:
#     print('ValueError')
# else:
#     print(min(s1),max(s1))
# print(sorted(set(s)))


# f=[3, 1, 2, 1, 3] 
# print(sorted(set(f)))

# x=[]
# print(sorted(set(x)))

# y=[-1, -1, 0, 2, 2]
# print(sorted(set(y)))

# a=[1.0, 1, 2.5, 2.5, 0]
# b=[]
# c=[]
# for i in a:
#     if type(i)==int:
#         c.append(i)
#     else:
#         b.append(i)
# res1=[x for x in b if int(x) in c]
# res2=[x for x in c if float(x) not in b]
# print(sorted(set(res1+res2+b)))

a=[[1, 2],[3, 4]]
x=[]
y=[]
k=0
for i in a:
    for b in i:
        x.append(b)
        if type(b)==int:
            k+=1
        if k==len(x):
            y.append(b)
        else:
            print('TypeError')
if k==len(x):
    print(y)


