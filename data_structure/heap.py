class Heap:
	def __init__(self, array):
		self.array=array
		self.heapify(array, 1)
	
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

if __name__=="__main__":
	l=[3,2,13,1,33,6,8]
	heap=Heap(l)
	print (heap.array)
		
