from heap import Heap
from tree_node import dNode
from bst import BSTree

def read_text(text):
	"""
	read every characters in the text and record the frequencies of 
	each character.
	"""
	d={}
	for char in text:
		if char not in d:
			d[char]=0
		d[char]+=1	
	return d

def nodeKey(node, dic):
	"""
	generate the key of specified node.
	2 kinds of nodes exist in a Huffman coding tree:
	* frequency node : the value of it is the total 
	  frequencies of both left and right subtree
	* char node : the value of it is a actual character 
	  and both of its children are external nodes. 
	for frequencies node, the key of it is the value of the node.
	for char node, the key of it is the value associated with the char 
	in the given dictionary. 	
	"""
	if node.depth==0:
		return dic[node.val]
	else:
		return node.val


def huffman_coding(text):
	"""
	compress each charater in the given text (a collection of characters) 
	into a uniquely identifiable binary number. 
	"""
	frequencies=read_text(text)
	pq=[]
	heap=Heap(pq, lambda x: nodeKey(x, frequencies))
	for char in frequencies:
		heap.push(pq, dNode(char, None, None))
	while (len(pq)>1):
		left=heap.removeMin(pq)
		right=heap.removeMin(pq)
		internal_key=nodeKey(left, frequencies)+\
			nodeKey(right, frequencies)
		heap.push(pq, dNode(internal_key, left, right, \
			max(left.depth, right.depth)+1))
	return heap.removeMin(pq)

def compress(text):
	tree=BSTree()
	tree.root=huffman_coding(text)
	

if __name__=="__main__":
	compress("You are ")
