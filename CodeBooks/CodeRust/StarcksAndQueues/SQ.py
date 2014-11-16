#!/usr/bin/env python3
# use Stack to implement Queue
from Stack import Stack

class SQueue(object):
    """
    docstring for SQueue
    use Stack to implement Queue
    use enq_s to store enqueue items
    use deq_s to store dequeue items
    put enq_s into deq_s, only when deq_s is empty
    """
    def __init__(self):
        self.deq_s = Stack()
        self.enq_s = Stack()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, item):
        print('Enqueue item %d' %item)
        self.enq_s.push(item)
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            print('Empty Queue.')
            return None
        if self.deq_s.is_empty():
            self._transfer_items()
        item = self.deq_s.pop()
        print('Dequeue item %d' %item)
        self._size -= 1
        return item

    def _transfer_items(self):
        '''Transfer items from enq_s to deq_s'''
        while not self.enq_s.is_empty():
            self.deq_s.push(self.enq_s.pop())


if __name__ == '__main__':
    q = SQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    q.dequeue()
    q.enqueue(5)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()