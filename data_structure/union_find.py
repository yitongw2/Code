
class UnionFind:
	def __init__(self, clusters=[]):
		# labels 
		self.clusters = set(clusters)
		
		# uni_set = a dictionary where key is element 
		# and value is a pair of (label, size)
		self.uni_set = dict([(x,[x,1]) for x in self.clusters])

	def makeSet(self, e):
		"""
		Create a singleton set containing the element e 
		and return the position storing e in this set
		"""
		self.uni_set[e] = [e,1]
		self.clusters.add(e)
	
	def root(self, v):
		"""
		find the root label of the element v.
		a root label is a node where its label is its element
		"""
		while (v != self.uni_set[v][0]):
			# path compression 
			# if we find a node's parent label and it is not root,
			# we can update it to the parent label of v's parent
			# label
			self.uni_set[v][0] = self.uni_set[self.uni_set[v][0]][0]
			v = self.uni_set[v][0]
		return (v, self.uni_set[v][1])
	
	def union(self, A, B):
		"""
		Return the set A U B, naming the result “A” or “B” 
		"""
		rootA, sizeA = self.root(A)
		rootB, sizeB = self.root(B)
		if sizeA < sizeB:
			self.uni_set[rootA][0] = rootB
			self.uni_set[rootB][1] = sizeA+sizeB  	
			self.clusters.remove(rootA)
		else:
			self.uni_set[rootB][0] = rootA
			self.uni_set[rootA][1] = sizeA+sizeB
			self.clusters.remove(rootB)
	
	def find(self, A):
		"""
		Return the set containing the element e
		"""	
		return self.root(A)[0]
	
	def clusters_size(self):
		return len(self.clusters)
	
	def __iter__(self):
		for cluster in self.clusters:
			yield cluster
	
	def print(self):
		for x in self.uni_set:
			rootX,sizeX = self.root(x)
			print ("element:",x," cluster:",rootX," size:",sizeX)


if __name__ == "__main__":
	uf = UnionFind([0,1,2,3,4,5,6,7,8,9])
	uf.union(3,4)
	print (3,4)
	uf.print()
	uf.union(4,9)
	print (4,9)
	uf.print()
	uf.union(8,0)
	print (8,0)
	uf.print()
	uf.union(2,3)
	print (2,3)
	uf.print()
	uf.union(5,6)
	print (5,6)
	uf.print()
	print (5,9)
	uf.union(5,9)
	uf.print()
	print (7,3)
	uf.union(7,3)
	uf.print()
	print (4,8)
	uf.union(4,8)
	uf.print()
	print (6,1)
	uf.union(6,1)
	uf.print()
	print (uf.find(0))
	uf.print()
