# python_labs

# Лабораторная работа 1
## Задание 1
```python
a=input("Имя:")
b=int(input("Возраст: "))
c=b+1
print(f"Привет, ",a,"! Через год тебе будет",c)
```
![alt text](image1/01.png)
## Задание 2
```python
a=input('a: ')
a=a.replace(',','.')
a=float(a)
b=input('b: ')
b=b.replace(',','.')
b=float(b)
print(f"sum={a+b}; avg={(a+b)/2:.2f}")
```
![alt text](image1/02.png)
## Задание 3
```python
price=float(input('цена, р: '))
discount=float(input('скидка, %: '))
vat=float(input('ндс, %:'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"база после скидки:{base:.2f} р")
print(f"ндс:{vat_amount:.2f} р")
print(f"итого к оплате:{total:.2f} р")
```
![alt text](image1/03.png)
## Задание 4
```python
m=int(input("минуты: "))
print(f"{m//60}:{m-(60*(m//60)):02d}")
```
![alt text](image1/04.png)
## Задание 5
```python
name=str(input("ФИО: "))
print(f"инициалы: {(name.split()[0])[0]}{(name.split()[1])[0]}{(name.split()[2])[0]}.")
name=name.replace(' ','')
print(f"длина: {len(name)+2}")
```
![alt text](<image1/image copy.png>)
## Задание 6
```python
n=int(input('in_1: '))
k=1
och=0
zao=0
for i in range(n):
    k+=1
    name1, name2,voz , obu = (input(f'in{k}: ')).split()
    if obu=="True":
        och+=1
    else:
        zao+=1
print(f'out: {och},{zao}')
```
![alt text](image1/image.png)


# Лабораторная работа 2
## Задание 1
###1
```python
a=[3,-1,5,5,0]
b=[42]
c=[-5, -2, -9]
d=[]
e=[1.5, 2, 2.0, -3.1]
def f(b):
    a=tuple(b)
    s1=[]
    for i in a:
        s1.append(i)
    if len(s1)==0:
        print('ValueError')
    else:
        s2=(min(s1),max(s1))
        print(s2)
print(f(a))
print(f(b))
print(f(c))
print(f(d))
print(f(e))
```

![alt text](<image2/image 2.1.1.png>)

```python
a=[3, 1, 2, 1, 3] 
b=[]
c=[-1, -1, 0, 2, 2]
d=[1.0, 1, 2.5, 2.5, 0]
def f(a):
    g=[]
    h=[]
    for i in a:
        if type(i)==int:
            h.append(i)
        else:
            g.append(i)
    res1=[x for x in g if int(x) in h]
    res2=[x for x in h if float(x) not in g]
    print(sorted(set(res1+res2+g)))
print(f(a))
print(f(b))
print(f(c))
print(f(d))
```
![alt text](<image2/image 2.1.2.png>)

```python
a=[[1, 2], [3, 4]]
b=([1, 2], (3, 4, 5))
c=[[1], [], [2, 3]]
d=[[1, 2], "ab"]

def f(a):
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

print(f(a))
print(f(b))
print(f(c))
print(f(d))
```
![alt text](<image2/image 2.1.3.png>)

##Задание 2
```python
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
```
![alt text](<image2/image 2.2.1.png>)

```python
a=[[1, 2, 3], [4, 5, 6]] 
b=[[-1, 1], [10, -10]] 
c=[[0, 0], [0, 0]] 
d=[[1, 2], [3]]
def f(x):
    for i in range(len(x)-1):
        if len(x[i])!=len(x[i+1]):
            print("ValueError")
        else:
            return [sum(x[i]),sum(x[i+1])]
print(f(a))
print(f(b))
print(f(c))
print(f(d))      
```
![alt text](<image2/image 2.2.2.png>)

```python
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
```
![alt text](<image2/image 2.2.3.png>)

##Задание 3
```python
def f(x):
    if type(x[0]) == str:
        e=x[0].split()
        if len(e)==2:
            f=e[0].capitalize()+' '+(e[1].capitalize())[0]+'.'
        else:
            f=e[0].capitalize()+' '+ (e[1].capitalize())[0]+'.'+(e[2].capitalize())[0]+'.'
        res=f+','+' гр.'+x[1] + ', ' + f"{x[2]:.2f}"
        print(res)
        

a = ("Иванов Иван Иванович", "BIVT-25", 4.6)
b=("Петров Пётр", "IKBO-12", 5.0) 
c=("Петров Пётр Петрович", "IKBO-12", 5.0) 
d=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
print(f(a))
print(f(b)) 
print(f(c)) 
print(f(d))  
```
![alt text](<image2/image 2.3.png>)