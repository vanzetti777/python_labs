from lab10.structures import Stack, Queue
from lab10.linked_list import SinglyLinkedList

def test_stack():
    print("тест стека")
    s = Stack()
    print("пустой стек создан")
    
    # тест push и peek
    s.push(1); s.push(2)
    print(f"push(1), push(2) выполнено")
    print(f"peek() = {s.peek()} (ожидается 2)")
    
    # тест pop
    print(f"pop() = {s.pop()} (ожидается 2)")
    print(f"pop() = {s.pop()} (ожидается 1)")
    print(f"is_empty() = {s.is_empty()} (ожидается true)")
    
    # тест исключения
    try:
        s.pop()
    except IndexError as e:
        print(f"исключение при pop() из пустого стека: {e}")
    
    print("ура стек работает\n")

def test_queue():
    print("тест очереди")
    
    q = Queue()
    print("пустая очередь создана")
    
    # тест enqueue и peek
    q.enqueue(1); q.enqueue(2)
    print(f"enqueue(1), enqueue(2) выполнено")
    print(f"peek() = {q.peek()} (ожидается 1)")
    
    # тест dequeue
    print(f"dequeue() = {q.dequeue()} (ожидается 1)")
    print(f"dequeue() = {q.dequeue()} (ожидается 2)")
    print(f"is_empty() = {q.is_empty()} (ожидается true)")
    
    # тест исключения
    try:
        q.dequeue()
    except IndexError as e:
        print(f"исключение при dequeue() из пустой очереди: {e}")
    
    print("ура очередь работает\n")

def test_linked_list():
    print("тест списка\n")
    lst = SinglyLinkedList()
    print(f"пустой список создан, len={len(lst)}\n")
    
    # тест append
    lst.append(1); lst.append(2); lst.append(3)
    print(f"append(1,2,3)")
    print(f"список: {lst}")
    print()
    
    # тест prepend
    lst.prepend(0)
    print(f"prepend(0)")
    print(f"список: {lst}")
    print()
    
    # тест insert
    lst.insert(2, 1.5)
    print(f"insert(2, 1.5)")
    print(f"список: {lst}")
    print()
    
    lst.insert(0, -1)
    print(f"insert(0, -1)")
    print(f"список: {lst}")
    print()
    
    lst.insert(len(lst), 4)
    print(f"insert({len(lst)-1}, 4)")
    print(f"список: {lst}")
    print()
    
    print(f"list(lst) = {list(lst)}\n")
    
    # тест remove_at
    lst.remove_at(2)
    print(f"remove_at(2) - удалили элемент на позиции 2")
    print(f"список: {lst}")
    print()
    
    lst.remove_at(0)
    print(f"remove_at(0) - удалили первый элемент")
    print(f"список: {lst}")
    print()
    
    lst.remove_at(len(lst)-1)
    print(f"remove_at({len(lst)-1}) - удалили последний элемент")
    print(f"список: {lst}")
    print()

    # тест __iter__
    print(f"итерация по списку: {[x for x in lst]}\n")
    
    # тест __len__
    print(f"длина списка: {len(lst)}\n")
    
    # тест __repr__
    print(f"repr списка: {repr(lst)}\n")
    
    # тест исключений
    try:
        lst.insert(10, 5)
    except IndexError as e:
        print(f"исключение insert(10,5): {e}\n")
    
    try:
        lst.remove_at(10)
    except IndexError as e:
        print(f"исключение remove_at(10): {e}\n")
    
    print(f"итоговый список: {lst}")
    print(f"итоговая длина: {len(lst)}")

if __name__ == "__main__":
    test_stack()
    print("@" * 40)
    test_queue()
    print("@" * 40)
    test_linked_list()
    print("\nвсе тесты завершены")
