class Heap:
	def __init__(self, array):
		self.array=array
		self.heapify(array, 1)
	
	def heapify(self, arr, index):
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
		if left<=len(arr) and arr[left-1]<arr[parent-1]:		
			parent=left
		if right<=len(arr) and arr[right-1]<arr[parent-1]:
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
		if parent>0 and arr[parent-1]>arr[index-1]:
			temp=arr[parent-1]
			arr[parent-1]=arr[index-1]
			arr[index-1]=temp
			self.upward_rotate(arr, parent)	

	def insert(self, key):
		self.array.append(key)
		self.upward_rotate(self.array, len(self.array))
	
	
if __name__=="__main__":
	l=[3,2,13,0,23,1,33,4,6]
	heap=Heap(l)
	heap.insert(0)
	print (heap.array)
		
