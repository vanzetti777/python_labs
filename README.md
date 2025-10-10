# python_labs

# Лабораторная работа 1
## Задание 1
```python
a=input("Имя:")
b=int(input("Возраст: "))
c=b+1
print(f"Привет, ",a,"! Через год тебе будет",c)
```
![!\[alt text\](image1/01.png)](img/image1/01.png)
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
![!\[alt text\](image1/02.png)](img/image1/02.png)
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
![!\[alt text\](image1/03.png)](img/image1/03.png)
## Задание 4
```python
m=int(input("минуты: "))
print(f"{m//60}:{m-(60*(m//60)):02d}")
```
![!\[alt text\](image1/04.png)](img/image1/04.png)
## Задание 5
```python
name=str(input("ФИО: "))
print(f"инициалы: {(name.split()[0])[0]}{(name.split()[1])[0]}{(name.split()[2])[0]}.")
name=name.replace(' ','')
print(f"длина: {len(name)+2}")
```
![!\[alt text\](<image1/image copy.png>)](<img/image1/image copy.png>)
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
![!\[alt text\](image1/image.png)](img/image1/image.png)


# Лабораторная работа 2
## Задание 1
```python
test1=[3,-1,5,5,0]
test2=[42]
test3=[-5, -2, -9]
test4=[]
test5=[1.5, 2, 2.0, -3.1]
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    #проверка на пустой список
    if len(nums)==0:
        print('ValueError')
    else:
        list2=(min(nums),max(nums))
        print(list2)
print(min_max(test1))
print(min_max(test2))
print(min_max(test3))
print(min_max(test4))
print(min_max(test5))
```

![!\[alt text\](<image2/image 2.1.1.png>)](<img/image2/image 2.1.1.png>)

```python
test1=[3, 1, 2, 1, 3] 
test2=[]
test3=[-1, -1, 0, 2, 2]
test4=[1.0, 1, 2.5, 2.5, 0]
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    #создаем 2 списка
    list_int=[]
    list_float=[]
    #разделяю инт и флоат 
    for i in nums:
        if type(i)==int:
            list_int.append(i)
        else:
            list_float.append(i)
    res1=[x for x in list_float if int(x) in list_int]#добавляю флоат если он в инт значении есть в инт списке
    res2=[x for x in list_int if float(x) not in list_float]#добавляю инт если во флоат его нет
    print(sorted(set(res1+res2+list_float)))
print(unique_sorted(test1))
print(unique_sorted(test2))
print(unique_sorted(test3))
print(unique_sorted(test4))
```
![!\[alt text\](<image2/image 2.1.2.png>)](<img/image2/image 2.1.2.png>)

```python
test1=[[1, 2], [3, 4]]
test2=([1, 2], (3, 4, 5))
test3=[[1], [], [2, 3]]
test4=[[1, 2], "ab"]

def flatten(mat: list[list | tuple]) -> list:
    #создаю 2 списка чтобы все забрать в списки
    list1=[]
    list2=[]
    count=0
    #перебираю элементы списка/кортежа
    for enum1 in mat:
        #перебираю элементы в элементах..и все добавляю в 1 список
        for enum2 in enum1:
            list1.append(enum2)
            #проверка на матричность элемента
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
![!\[alt text\](<image2/image 2.1.3.png>)](<img/image2/image 2.1.3.png>)

##Задание 2
```python
test1=[[1, 2, 3]]
test2=[[1], [2], [3]] 
test3=[[1, 2], [3, 4]] 
test4=[] 
test5=[[1, 2], [3]]
def transpose(mat: list[list[float | int]]) -> list[list[float | int]]:
    #обработка пустой матрицы
    if not mat:
        return []
    #проверка на равные елементы
    row1st = len(mat[0])
    for row in mat:
        if len(row) != row1st:
            return ("ValueError")
    #транспоз
    transp = []
    for col_index in range(len(mat[0])):
        row_new = []
        for row_index in range(len(mat)):
            row_new.append(mat[row_index][col_index])
        transp.append(row_new)
    return transp
print(transpose(test1))
print(transpose(test2))
print(transpose(test3))
print(transpose(test4))
print(transpose(test5))
```
![!\[alt text\](<image2/image 2.2.1.png>)](<img/image2/image 2.2.1.png>)

```python
test1=[[1, 2, 3], [4, 5, 6]] 
test2=[[-1, 1], [10, -10]] 
test3=[[0, 0], [0, 0]] 
test4=[[1, 2], [3]]
def row_sums(mat: list[list[float | int]]) -> list[float]:
    #проверяю на одинак длину элементов
    for i in range(len(mat)-1):
        if len(mat[i])!=len(mat[i+1]):
            print("ValueError")
        else:
            #беру сумму по элементам списка
            return [sum(mat[i]),sum(mat[i+1])]
print(row_sums(test1))
print(row_sums(test2))
print(row_sums(test3))
print(row_sums(test4))          
```
![!\[alt text\](<image2/image 2.2.2.png>)](<img/image2/image 2.2.2.png>)

```python
test1=[[1, 2, 3], [4, 5, 6]]
test2=[[-1, 1], [10, -10]] 
test3=[[0, 0], [0, 0]] 
test4=[[1, 2], [3]]
def col_sums(mat: list[list[float | int]]) -> list[float]:
    #проверяю пары из списка на одинак длину
    for enum1 in range(len(mat)-1):
        if len(mat[enum1])!=len(mat[enum1+1]):
            print("ValueError")
        else:
            #беру сумму по каждому столбцу
            list1 = []
            for enum2 in zip(*mat): 
                list1.append(sum(enum2))
    return list1
print(col_sums(test1))
print(col_sums(test2))
print(col_sums(test3))
print(col_sums(test4))
```
![img/image2/image 2.2.3.png](<img/image2/image 2.2.3.png>)

## Задание 3

```python
def format_record(rec: tuple[str, str, float]) -> str:
    #проверяю на пустые ячейки
    if len(rec) != 3:
        return ValueError
    #проверяю гпа на правильность
    if not isinstance(rec[2], (int, float)):
        return TypeError
    if rec[2] < 0 or rec[2] > 5.0:
        return ValueError
    #проверяю фио, разделяю и беру только большие буквы
    if type(rec[0]) == str:
        e=rec[0].split()
        #если фи
        if len(e)==2:
            f=e[0].capitalize()+' '+(e[1].capitalize())[0]+'.'
        else:
            f=e[0].capitalize()+' '+ (e[1].capitalize())[0]+'.'+(e[2].capitalize())[0]+'.'
        res=f+','+' гр.'+rec[1] + ', ' + f"{rec[2]:.2f}"
        print(res)
        

test1 = ("Иванов Иван Иванович", "BIVT-25", 4.6)
test2=("Петров Пётр", "IKBO-12", 5.0) 
test3=("Петров Пётр Петрович", "IKBO-12", 5.0) 
test4=("  сидорова  анна   сергеевна ", "ABB-01", 3.999)
test5=( "ABB-01", 3.999)
test6=("Петров Пётр Петрович", "IKBO-12", 6.0) 
print(format_record(test1))
print(format_record(test2)) 
print(format_record(test3)) 
print(format_record(test4))  
print(format_record(test5)) 
print(format_record(test6)) 
```
![img/image2/image 2.3.png](<img/image2/image 2.3.png>)

# Лабораторная работа 3
## Задание 1
```python
testcase1="ПрИвЕт\nМИр\t"
testcase2="ёжик, Ёлка" 
testcase3="Hello\r\nWorld" 
testcase4="  двойные   пробелы  "
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    # r'\s+' заменяем все все лишние элементы, заменяет на пробел
    text= re.sub(r'\s+', ' ', text).strip()
    text=text.casefold()
    text=text.replace('ё','e')
    return text
    
print(normalize(testcase1))
print(normalize(testcase2))
print(normalize(testcase3))
print(normalize(testcase4))

testcase1="привет мир" 
testcase2="hello,world!!!"
testcase3="по-настоящему круто" 
testcase4="2025 год"
testcase5="emoji 😀 не слово"

import re
def tokenize(text: str) -> list[str]:
    shablon=r'\w+(?:-\w+)*'
    # ищет все по шаблону из норм текста 
    tockens = (re.findall(shablon,normalize(text)))
    return tockens

print(tokenize(testcase1))
print(tokenize(testcase2))
print(tokenize(testcase3))
print(tokenize(testcase4))
print(tokenize(testcase5))

testcase1=["a","b","a","c","b","a"]
testcase2=["bb","aa","bb","aa","cc"]

def count_freq(tokens: list[str]) -> dict[str, int]:
    fdict={}
    #создаем словарь
    for token in tokens:
        # если в словаре есть например 'а' то счетчик "a" увеличивается 
        if token in fdict:
            fdict[token]+=1
        else:
            fdict[token]=1
    return fdict

#УЖЕ ПОСЛЕ СОЗДАНИЯ СЛОВАРЯ ИЗ ЭЛЕМЕНТОВ
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    #превращем в представление словаря в списке
    items = list(freq.items())
    
    # Сортируем сначала по убыванию частоты, потом по алф
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    # Возвращаем первые N элементов
    return sorted_items[:n]


print(count_freq(testcase1))
print(top_n(count_freq(testcase1)))
print(count_freq(testcase2))
print(top_n(count_freq(testcase2)))
```
![alt text](img/image3/03.01.png)
# Задание 2
``` python
import sys
import text 

stdin = sys.stdin.read()
#все слова списком
allwords= text.tokenize(stdin)
#уник слова списком
uniquewords=text.count_freq(allwords)
#слово и частота списком
top= text.top_n(uniquewords,5)
print(f'Всего слов: {len(allwords)}')
print(f'Уникальных слов: {len(uniquewords)}')
print("Топ-5:")
for i in top:
    print(i[0]+':'+str(i[1])) 
```
![alt text](img/image3/03.02.png)
