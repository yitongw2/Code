class Node:
	def __init__(self, value, left, right):
		self.left=left
		self.right=right
		self.val=value


class BSTree:
	def __init__(self):
		self.root=None
	
	def insert(self, val):
		self.root=self._insert(val, self.root)
	
	def _insert(self, val, node):
		if node==None:
			return Node(val, None, None)
		else:
			if node.val==val:
				return node 
			elif node.val>val:
				node.left=self._insert(val, node.left)
			else:
				node.right=self._insert(val, node.right)
			return node	
	
	def remove(self, val):
		self._remove(val, self.root)

	def _remove(self, val, node):
		if node==None:
			return None 
		else:
			if node.val==val:
				if node.left!=None and node.right!=None:
					closest=self._find_leftmost(node.right)
					temp=closest.val
					closest.val=node.val
					node.val=temp
					node.right=self._remove(val, node.right)
					return node
				elif node.left!=None:
					return node.left
				else:
					return node.right
			elif node.val<val:
				node.right=self._remove(val, node.right)
				return node
			else:
				node.left=self._remove(val, node.left)
				return node
	
	# private function
	def _find_leftmost(self, node):
		if node.left==None:
			return node
		else:
			return self._find_leftmost(node.left)
	
	def print(self, node, count):
		if node!=None:
			self.print(node.left, count+1)
			print (node.val, "level=", count)
			self.print(node.right, count+1)


if __name__=="__main__":
	t=BSTree()
	t.insert(3)
	t.insert(6)
	t.insert(2)
	t.insert(1)
	t.insert(5)
	t.insert(7)
	t.print(t.root, 0)
	print ()
	print (t._find_leftmost(t.root.right).val)
	print ()
	t.remove(3)
	t.print(t.root, 0)
	print()
	t.remove(5)
	t.print(t.root, 0) 
	print ()
	t.remove(0)
	t.print(t.root, 0)
