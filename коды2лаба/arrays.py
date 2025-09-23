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
# print(set(sorted(res1+res2+b)))


