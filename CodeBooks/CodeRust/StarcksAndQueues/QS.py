#!/usr/bin/env python3
# Use Queue to implement Stack
from Queue import Queue

class QStack(object):
    """
    Use Queue to implement Stack
    q1 always contain items
    q2 uses for pop item
    iterate all items store from q1 to q2
    keep the last q1 item, then pop it
    """
    def __init__(self):
        self._q1 = Queue()
        self._q2 = Queue()
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        print('Push item %d' %item)
        self._q1.enqueue(item)
        self._size += 1

    def pop(self):
        if self.is_empty():
            print('Stack is empty.')
            return None
        idx = self._size
        while idx > 1:
            self._q2.enqueue(self._q1.dequeue())
            idx -= 1
        else:
            item = self._q1.dequeue()
            self._size -= 1
            self._q1, self._q2 = self._q2, self._q1
        print('Pop item %d' %item)
        return item


if __name__ == '__main__':
    s = QStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(10)
    print(s)
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()