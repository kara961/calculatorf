class Stack:
	def __init__(self):
		self._data = []
	
	def push(self, item):
		self._data.append(item)

	def peek(self):
		if not self._data:
			return None
		
		return self._data[-1]

	def pop(self):
		if not self._data:
			return None
		return self._data.pop()

	def is_empty(self):
		return len(self._data) == 0

	def __str__(self):
		return " ".join(reversed(self._data))

	def __len__(self):
		return len(self._data)