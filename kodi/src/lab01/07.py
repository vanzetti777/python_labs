s=str(input( 'in: '))
word=[]
id_1 = 0
id_2 = 0
id_p = 0
for i in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
    if i in s:
        id_1 = s.index(1)
for j in '0123456789':
    if (j in s):
        id_2=s.index(j)+1
        break
id_p=s. index('.')
zar=id_2-id_1
for i in range (id_1, id_p+1, zar) :
    word.append (s[i])
print(f'out: {'' . join (word)}')