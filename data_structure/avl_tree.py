from bst import BSTree
from tree_node import dNode

class AVLTree(BSTree):
	def __init__(self):
		"""
		AVL tree is essentailly a binary search tree and inherits the 
		property of a binary search tree (left subtree < parent and 
		right subtree > parent). 
		"""
		BSTree.__init__(self)

	def insert(self, val):
		"""
		calls private function _insert() for recursive insertion
		"""
		self.root=self._insert(val, self.root)
	
	def _insert(self, val, node):
		"""
		a recursive function for insertion.
		recurrence: 
		  * when node is leaf node, insert the new node here and 
		    return the newly inserted node.
	          * when node is not leaf node, binary search the right path 
		    to go; for each recursive call, update the left/right node
		    based on the result from the last recursive call and 
		    increment the depth by one. 		
		"""
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
					return self._trinode_rotate(node)
				elif node.left!=None:
					return node.left
				elif node.right!=None:
					return node.right
				else:
					return None
			elif node.val<val:
				node.right=self._remove(val, node.right)
				self.set_depth(node)
				return self._trinode_rotate(node)
			else:
				node.left=self._remove(val, node.left)
				self.set_depth(node)
				return self._trinode_rotate(node)
	
	def _LL_rotate(self, node):
		n_parent=node.left
		node.left=n_parent.right
		n_parent.right=node
		self.set_depth(node)
		self.set_depth(n_parent)	
		return n_parent

	def _RR_rotate(self, node):
	 	n_parent=node.right
	 	node.right=n_parent.left
	 	n_parent.left=node
	 	self.set_depth(node)
	 	self.set_depth(n_parent)
	 	return n_parent

	def _trinode_rotate(self, node):
		n_parent=node
		if self._depth(node.left)-self._depth(node.right)>1:
			if self._depth(node.left.right)>\
				self._depth(node.left.left):
				n_parent.left=self._RR_rotate(node.left)
			return self._LL_rotate(n_parent)
		elif self._depth(node.right)-self._depth(node.left)>1:
			if self._depth(node.right.left)>\
				self._depth(node.right.right):
				n_parent.right=self._LL_rotate(node.right)
			return self._RR_rotate(n_parent)
		else:
			self.set_depth(n_parent)
			return n_parent		
	
	def set_depth(self, n):
		if n!=None:
			n.depth=max(self._depth(n.left)+1, self._depth(n.right)+1)

	def _depth(self, node):
		if node==None:
			return -1
		else:
			return node.depth



if __name__=="__main__":
	avl=AVLTree()
	avl.insert(0)
	avl.insert(2)
	avl.insert(6)
	avl.insert(7)
	avl.insert(8)
	avl.insert(10)
	avl.insert(9)
	avl.insert(-1)
	avl.remove(7)
	avl.remove(2)
	avl.print(avl.root, 0)
	#avl.print(avl.root)
	print (avl.search(8))
	print (avl.search(7))
