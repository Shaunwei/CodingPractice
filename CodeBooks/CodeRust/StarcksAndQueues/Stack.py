#!/usr/bin/env python3

# Implementation of Stack using list

class Stack(object):
	"""docstring for Stack"""
	def __init__(self, size=0):
		self._stack = list()
		self._size = size

	def __len__(self):
		return len(self._stack)

	def push(self, item):
#		print('input item: %d' %item)
		self._stack.append(item)
		self._size += 1

	def pop(self):
		if len(self) > 0:
			item = self._stack.pop()
			#print('pop item: %d' %item)
			return item
		else:
			print("Stack is empty.")

	def is_empty(self):
		return len(self._stack) == 0

	def __unicode__(self):
		print(self._stack)

	def __str__(self):
		return str(self._stack)

if __name__ == '__main__':
	s = Stack()
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