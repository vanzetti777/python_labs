s=list(input().split())
s1=[]
for i in s:
    if '.' in i:
        s1.append(float(i))
    else:
        s1.append(int(i))

if len(s1)==0:
    print('ValueError')
else:
    print(min(s1),max(s1))
print(sorted(set(s)))