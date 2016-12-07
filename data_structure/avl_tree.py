from bst import BSTree
from tree_node import dNode


class AVLTree(BSTree):
	def __init__(self):
		BSTree.__init__(self)

	def insert(self, val):
		self.root=self._insert(val, self.root)
	
	def _insert(self, val, node):
		if node==None:
			return dNode(val, None, None)
		else:
			if  node.val>val:
				node.left=self._insert(val, node.left)
				node.depth+=1
			elif node.val<val:
				node.right=self._insert(val, node.right)
				node.depth+=1
			return self._trinode_rotate(node)			

	def remove(self, val):
		self.root=self._remove(val, self.root)	
	
	def _trinode_rotate(self, node):
		if self._depth(node.left)-self._depth(node.right)>1:
			n_parent=node.left
			node.left=n_parent.left.right
			n_parent.right=node
			return n_parent
		elif self._depth(node.right)-self._depth(node.left)>1:
			n_parent=node.right
			node.right=n_parent.right.left
			n_parent.left=node
			return n_parent
		else:
			return node			
	
	def _depth(self, node):
		if node==None:
			return -1
		else:
			return node.depth

if __name__=="__main__":
	avl=AVLTree()
	avl.insert(3)
	avl.insert(2)
	avl.insert(1)
	avl.insert(7)
	avl.insert(4)
	avl.insert(0)
	avl.print(avl.root, 0)
	print (avl.search(8))
	print (avl.search(7))
