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

	def _remove(self, val, node):
		"""
		a recursive funtion for removing a specified item from the tree
		recurrence:
			* when the node is leaf node, no removal is performed
			  since the specified item is not found.
			* when node is not leaf node, binary search for the node
			  to be removed 
			* when find the correct node to be removed, 
			  - if the node has 2 non-external children, swap the 
			    value of the node with the node in its subtree that
		            has the closest value and continue the process 
			    downward
			  - if the node has 1 non-external child, reconnect its 			    child with the grandparent of the child.
			  - if the nodes has 0 non-external child, simply delete			    it by connecting the external node.
						
		"""
		if node==None:
			return None
		else:
			if node.val==val:
				if node.left!=None and node.right!=None:
					closest=self._find_leftmost(node.right)
					self._swap_node_val(closest, node)
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
				return self._trinode_rotate(node)
			else:
				node.left=self._remove(val, node.left)
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
	
	def printR(self, node):
		if node!=None:
			self.printR(node.left)
			print ("*"*node.depth, node.val)
			self.printR(node.right)


if __name__=="__main__":
	avl=AVLTree()
	avl.insert(0)
	avl.insert(2)
	avl.insert(6)
	avl.insert(7)
	avl.insert(8)
	avl.remove(6)
	avl.insert(10)
	avl.insert(9)
	avl.insert(-1)
	avl.remove(7)
	avl.remove(2)
	avl.insert(3)
	avl.insert(4)
	avl.print(avl.root, 0)
	print()
	avl.printR(avl.root)
	print (avl.search(8))
	print (avl.search(7))
	l=[]
	avl.range_query(avl.root, 2, 8, l)
	print (l)
