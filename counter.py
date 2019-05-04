from linked import LinkedList
from itertools import tee


class InsertCounter(LinkedList):

    def __init__(self):
        super().__init__()
        self._counter = 0

    def insert(self, value):
        super().insert(value)
        self._counter += 1

    def insert_all(self, iterable):
        iter1, iter2 = tee(iterable)
        super().insert_all(iter1)
        self._counter += sum(1 for _ in iter2)

    @property
    def counter(self):
        return self._counter
	

lst = InsertCounter()
lst.insert(4)
lst.insert_all([8, 15, 16, 23, 42])
lst.remove()
print(lst)
print(f'length  = {len(lst)}')
print(f'counter = {lst.counter}')
