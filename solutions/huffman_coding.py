from heap import Heap
from tree_node import Node
from bst import BSTree

def read_text(text):
	d={}
	for char in text:
		if char not in d:
			d[char]=0
		d[char]+=1	
	return d

def huffman_coding(text):
	frequencies=read_text(text)
	pq=[]
	heap=Heap(pq, lambda x: frequencies[x.val])
	for char in frequencies:
		heap.push(pq, Node(char, ))
	while (len(pq)>1):
		left_node=heap.removeMin(pq)
		right_node=heap.removeMin(pq)
		left_key=frequencies[left_node.val]
		right_key=frequencies[right_node.val]
		internal_key=left_key+right_key
		heap.push(pq, Node(internal_key, left_node, right_node))
	return heap.removeMin(pq)

if __name__=="__main__":
	huffman_coding("absdfawbsdx")
	

