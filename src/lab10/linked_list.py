from typing import Any, Optional, Iterator

class Node:
    # узел односвязного списка
    
    def __init__(self, value: Any, next_node: Optional['Node'] = None):

        self.value = value
        self.next = next_node
    
class SinglyLinkedList:
    # односвязный список
    
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        # добавить элемент в конец списка.

        new_node = Node(value)
        
        if self.head is None:  # Список пуст
            self.head = new_node
            self.tail = new_node
        else:  # Список не пуст
            self.tail.next = new_node  # type: ignore
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        # добавить элемент в начало списка.

        new_node = Node(value, self.head)
        self.head = new_node
        
        # если список был пуст, обновляем tail
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        #вставить элемент по индексу.

        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        # вставка в начало
        if idx == 0:
            self.prepend(value)
            return
        
        # вставка в конец
        if idx == self._size:
            self.append(value)
            return
        
        # вставка в середину
        current = self.head
        for _ in range(idx - 1):
            current = current.next  # type: ignore
        
        new_node = Node(value, current.next)  # type: ignore
        current.next = new_node  # type: ignore
        self._size += 1
    
    def remove_at(self, idx: int) -> None:

        # удалить элемент по индексу.

        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")
        
        # удаление первого элемента
        if idx == 0:
            self.head = self.head.next  # type: ignore
            # если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None
        else:
            # находим элемент перед удаляемым
            current = self.head
            for _ in range(idx - 1):
                current = current.next  # type: ignore
            
            # пропускаем удаляемый элемент
            current.next = current.next.next  
            
            # если удалили последний элемент, обновляем tail
            if current.next is None:  # type: ignore
                self.tail = current  # type: ignore
        
        self._size -= 1
    
    def __iter__(self) -> Iterator[Any]:
        #итератор по значениям списка
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        # количество элементов в списке
        return self._size
    
    def __repr__(self) -> str:
        """Репрезентативное строковое представление."""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
     