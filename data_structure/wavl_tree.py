from tree_node import dNode
from avl_tree import AVLTree

class WAVLTree(AVLTree):
	def __init__(self):
		AVLTree.__init__(self)
	
	def _insert(self, val, node):
		if node==None:
			return dNode(val, None, None, 1)
		else:
			if node.val>val:
				node.left=self._insert(val, node.left)
				return self._insert_rotate(node, node.left, node.right)
			elif node.val<val:
				node.right=self._insert(val, node.right)
				return self._insert_rotate(node, node.right, node.left)
			else:
				return node
	
	def _remove(self, val, node):
		if node==None:
			return None
		else:
			if node.val==val:
				if node.left!=None and node.right!=None:
					closest=self._find_leftmost(node.right)
					self._swap_node_val(closest, node)
					node.right=self._remove(val, node.right)
					return self._remove_rotate(node, \
						node.right, node.left)
				elif node.left!=None:
					return node.left
				elif node.right!=None:
					return node.right
				else:
					return None
			elif node.val<val:
				node.right=self._remove(val, node.right)
				return self._remove_rotate(node, node.right,\
					node.left)
			else:
				node.left=self._remove(val, node.left)
				return self._remove_rotate(node, node.left,\
					node.right)

		

	def _insert_rotate(self, parent, target, sibling):
		# calculate the rank difference of target node
		rd=self._rank_diff(parent, target)
		if rd==0:
			# calculate the rank difference of sibling node
			rs=self._rank_diff(parent, sibling)
			if rs==1:
			# if sibling has a rank difference of 1, we can safely
			# promote parent's rank and preserve the rank-diiferenc
			# property among parent, target and sibling by creating
			# a 1-2 node
				parent.depth+=1
				return parent
			elif rs==2:
				# when sibling has a rank difference of 2,
				# promotion is not safe since it will increase
				# sibling's rank difference to 3. Therefore,
				# we need a trinode rotation
				return self._trinode_rotate(parent)
		elif rd==1:
			# when target's rank difference is 1, then everything
			# is just perfect. just return the parent node.
			return parent
	
	def _remove_rotate(self, parent, target, sibling):
		rd=self._rank_diff(parent, target)
		if target==None and sibling==None:
			# parent has two external nodes
			parent.depth=1
			return parent
		elif rd==3:
			# when target has rank difference of 3 
			rs=self._rank_diff(parent, sibling)
			if rs==2:
				# when sibling has rank difference of 2
				# safe to demote parent's rank so that 
				# rank_diff(parent,target)==2 and 
				# rank_diff(parent,sibling)==1. 
				parent.depth-=1
				return parent
			else:
				# otherwise, sibling has rank difference of 1
				rsl=self._rank_diff(sibling, sibling.left)
				rsr=self._rank_diff(sibling, sibling.right)
				if rsl==2 and rsr==2:
					# if sibling's children both have rank
					# difference of 2, safe to demotion
					# parent and sibling so that rank
					# difference of target is 1 and
					# rank difference of sibling is 1. 
					parent.depth-=1
					sibling.depth-=1
					return parent
				else:
					return self._trinode_rotate(parent)	
		else:
			return parent

	def _rank_diff(self, np, nq):
		return self._depth(np)-self._depth(nq)

	def _depth(self, node):
		if node==None:
			return 0
		else:
			return node.depth			
	

if __name__=="__main__":
	import random
	w=WAVLTree()
	for x in range(20):
		w.insert(x)
	print ("Before removal, Rank ")
	w.printR(w.root)
	print ("\nTree")
	w.print(w.root)
	for x in range(20):
		r=random.randint(0,1)
		if r>0.7:
			w.remove(x)
		elif 0.3<r<0.6:
			w.insert(x*0.5)
	print("\nAfter Removal, Rank")
	w.printR(w.root)
	print("\nTree")
	w.print(w.root)
	print()
	l=[]
	w.inorder_traverse(w.root, lambda x: l.append(x.val))
	print (l)
