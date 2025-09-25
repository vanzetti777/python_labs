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