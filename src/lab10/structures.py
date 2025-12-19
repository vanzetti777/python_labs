from collections import deque
from typing import Any, Optional


class Stack:
    
    def __init__(self):
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        # добавить элемент на вершину стека
        self._data.append(item)
    
    def pop(self) -> Any:
        # удалить и вернуть верхний элемент стека
        if self.is_empty():
            raise IndexError("Нельзя выполнить pop из пустого стека")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        # вернуть верхний элемент стека без удаления
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        # проверить, пуст ли стек
        return len(self._data) == 0
    
    def __len__(self) -> int:
        # вернуть количество элементов в стеке
        return len(self._data)
    
    def __str__(self) -> str:
        # строковое представление стека
        return f"Stack({self._data})"
    
    def __repr__(self) -> str:
        # репрезентативное строковое представление
        return self.__str__()


class Queue:

    def __init__(self):
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        # добавить элемент в конец очереди
        self._data.append(item)
    
    def dequeue(self) -> Any:
        # удалить и вернуть первый элемент очереди

        if self.is_empty():
            raise IndexError("Нельзя выполнить dequeue из пустой очереди")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        # вернуть первый элемент очереди без удаления

        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        # проверить, пуста ли очередь
        return len(self._data) == 0
    
