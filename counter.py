from linked import LinkedList
from itertools import tee


class InsertCounter:

    def __init__(self, linked_list):
        self.linked_list = linked_list
        self._counter = 0

    def insert(self, value):
        self.linked_list.insert(value)
        self._counter += 1

    def insert_all(self, iterable):
        iter1, iter2 = tee(iterable)
        self.linked_list.insert_all(iter1)
        self._counter += sum(1 for _ in iter2)

    @property
    def counter(self):
        return self._counter

    def remove(self):
        return self.linked_list.remove()

    def clear(self):
        self.linked_list.clear()

    def __iter__(self):
        return self.linked_list.__iter__()

    def __str__(self):
        return self.linked_list.__repr__()

    def __len__(self):
        return self.linked_list.__len__()


lst = InsertCounter(LinkedList())
lst.insert(4)
lst.insert_all([8, 15, 16, 23, 42])
lst.remove()
print(lst)
print(f'length  = {len(lst)}')
print(f'counter = {lst.counter}')
