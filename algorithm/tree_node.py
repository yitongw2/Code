
class nNode:
	"""
	the tree node of a n-Ary tree
	val: the value the tree node contains
	size: how many pointers it can contain
	pointers: a collection (tuple here) of pointers that point to next tree node
	"""
	def __init__(self, value, *n_pointers):
		self.val=value
		self.size=len(n_pointers)
		self.pointers=n_pointers


class Node:
	#the tree node in a binary(2-Ary) tree
	def __init__(self, value, left, right):
		self.val=value
		self.left=left
		self.right=right

class dNode(Node):
	"""
	a special type of binary tree node with its depth in the tree 
	"""
	def __init__(self, val, left, right, depth=0):
		Node.__init__(self, val, left, right)
		self.depth=depth

