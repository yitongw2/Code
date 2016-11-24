class Stack:
	def __init__(self):
		self.arr=[]
	def top(self):
		return self.arr[self.size()-1]
	def pop(self):
		return self.arr.pop();
	def push(self, element):
		return self.arr.append(element)
	def size(self):
		return len(self.arr)


if __name__=="__main__":
	l=[1,4,2,35,56,21,2,7]
	s=Stack()
	for x in l:
		s.push(x)
	for x in l:
		print (s.pop())
