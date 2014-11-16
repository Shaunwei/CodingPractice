#!/usr/bin/env python3

# Implementation of Queue using list

class Queue(object):
    """docstring for Queue"""
    def __init__(self, size=0):
        self._queue = list()
        self._size = size

    def __len__(self):
        return len(self._queue)

    def enqueue(self, item):
        # print('Enqueue item: %d' %item)
        self._queue.append(item)

    def dequeue(self):
        if len(self)>0:
            item = self._queue.pop(0)
            # print('Dequeue item: %d' %item)
            return item
        else:
            print('Empty Queue.')

    def is_empty(self):
        return len(self._queue) == 0

    def size_of(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
