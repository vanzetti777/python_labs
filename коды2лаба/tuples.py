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