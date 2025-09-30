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
```python
test1=[3,-1,5,5,0]
test2=[42]
test3=[-5, -2, -9]
test4=[]
test5=[1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    list1=[]
    for i in nums:
        list1.append(i)
    if len(list1)==0:
        print('ValueError')
    else:
        list2=(min(list1),max(list1))
        print(list2)

print(min_max(test1))
print(min_max(test2))
print(min_max(test3))
print(min_max(test4))
print(min_max(test5))
```

![alt text](<image2/image 2.1.1.png>)

```python
test1=[3, 1, 2, 1, 3] 
test2=[]
test3=[-1, -1, 0, 2, 2]
test4=[1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    list_int=[]
    list_float=[]
    for i in nums:
        if type(i)==int:
            list_int.append(i)
        else:
            list_float.append(i)
    res1=[x for x in list_float if int(x) in list_int]
    res2=[x for x in list_int if float(x) not in list_float]
    print(sorted(set(res1+res2+list_float)))
print(unique_sorted(test1))
print(unique_sorted(test2))
print(unique_sorted(test3))
print(unique_sorted(test4))
```
![alt text](<image2/image 2.1.2.png>)

```python
test1=[[1, 2], [3, 4]]
test2=([1, 2], (3, 4, 5))
test3=[[1], [], [2, 3]]
test4=[[1, 2], "ab"]

def flatten(mat: list[list | tuple]) -> list:
    list1=[]
    list2=[]
    count=0
    for enum1 in mat:
        for enum2 in enum1:
            list1.append(enum2)
            if type(enum2)==int:
                count+=1
            if count==len(list1):
                list2.append(enum2)
            else:
                print('TypeError')
    if count==len(list1):
        print(list2)

print(flatten(test1))
print(flatten(test2))
print(flatten(test3))
print(flatten(test4))
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
    if len(x) != 3:
        return ValueError
    if not isinstance(x[2], (int, float)):
        return TypeError
    if x[2] < 0 or x[2] > 5.0:
        return ValueError
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
e=( "ABB-01", 3.999)
i=("Петров Пётр Петрович", "IKBO-12", 6.0) 
print(f(a))
print(f(b)) 
print(f(c)) 
print(f(d))  
print(f(e)) 
print(f(i)) 
```
![alt text](<image2/image 2.3.png>)