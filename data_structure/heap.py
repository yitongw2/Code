class Heap:
	def __init__(self, array, key=lambda x:x):
		self.arr = list(array)
		self.pri = dict([(x,key(x)) for x in self.arr])
		self.heapify(self.arr, 1)
			
	def heapify(self, arr, index):
		"""
			heapify: turn an array into a heap
			base case: extrnal nodes in the tree (in array, index > length of the array) 
			recursive case: split tree into left subtree and right subtree and rotate the tree if necessary
			time complexity: O(n) (for all n elements in the array)
						+
					 O(n) (at most O(n) rotations)
		"""
		if index>len(arr):
			return
		else:
			left=2*index
			right=left+1
			self.heapify(arr, left)
			self.heapify(arr, right)
			self.rotate(arr, index)
	
	def rotate(self, arr, index):
		"""
		Downward bubbling through the tree.
		At any given node N as parent node (specified by index in array), 
		if N has only left child:
			if N's left child is smaller than the parent node:
				swap parent node and its left child
				continue downward bubling starting at left child
		if N has both left and right child:
			choose the smallest node of parent node's children
			swap it with parent node
			continue downward bubling starting at the smallest child
		Otherwise:
			heap-order property is preserved
			no further rotation is needed
		"""

		parent=index
		left=2*index
		right=left+1
		if left<=len(arr) and self.pri[arr[left-1]]<self.pri[arr[parent-1]]:		
			parent=left
		if right<=len(arr) and self.pri[arr[right-1]]<self.pri[arr[parent-1]]:
			parent=right
		if parent!=index:
			temp=arr[index-1]
			arr[index-1]=arr[parent-1]
			arr[parent-1]=temp
			self.rotate(arr, parent)	
	
	def upward_rotate(self, arr, index):
		"""
		upward bubling from the rightmost external node of the tree.
		if the parent node is larger than the child node:
			swap them 
			continue upward starting at the new parent node
		Otherwise:
			order is preserved
			done
		"""
		parent=int(index/2)
		if parent>0 and self.pri[arr[parent-1]]>self.pri[arr[index-1]]:
			temp=arr[parent-1]
			arr[parent-1]=arr[index-1]
			arr[index-1]=temp
			self.upward_rotate(arr, parent)	

	def push(self, item, rank):
		"""	
		insert an element to the heap.
		perform an upward rotation if necessary
		"""
		self.arr.append(item)
		self.update(item, rank)	
		self.upward_rotate(self.arr, len(self.arr))
	
	def removeMin(self):
		"""
		remove the smallest  element from the heap.
		in the meantime, maintain the heap-order property after
		the removal. 
		"""
		temp=self.arr[0]
		self.arr[0]=self.arr[len(self.arr)-1]
		self.arr[len(self.arr)-1]=temp
		self.arr.pop()
		self.rotate(self.arr, 1)		
		return temp
	
	def update(self, item, rank):
		self.pri[item] = rank
		self.heapify(self.arr, 1)
		
	def size(self):
		return len(self.arr) 
	
if __name__=="__main__":
	l=[-1,3,2,13,23,1,33,4,6]
	heap=Heap(l)
	heap.push(0,0)
	print (l)
	left=heap.removeMin()
	right=heap.removeMin()
	print (l)
	print (left, right)
