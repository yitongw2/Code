import __init__
from graph import UndGraph, Vertex, Edge
from heap import Heap
from union_find import UnionFind

def prim_jarnik_mst(G, s):
	# cost of each vertex
	C = dict()
	# cheapest edge to each vertex
	E = dict()
	# setup
	for v in G.vertices():
		if v == s:
			C[v] = 0
		else:
			C[v] = 99999
	# priority queue 
	pq = Heap(G.vertices(), lambda x:C[x])
	# MST graph
	mst = UndGraph()
	
	while (pq.size()>0):
		v = pq.removeMin()
		mst.add_vertex(v)
		if E.get(v, False):
			mst.add_edge(E[v][0],v,E[v][1])
			print (E[v][0].info, v.info, E[v][1])
		for w,wei in G.neighbors(v):
			if w in pq.arr and C[w]>wei:
				C[w] = wei
				E[w] = (v,wei)
				pq.update(w,wei)
	
	return mst


def kruskal_mst(G):
	# initialize union-data structure
	uf = UnionFind()
	# undirected graph for minimum spanning tree		
	mst = UndGraph()
	# make every vertex as a single cluster
	for v in G.vertices():
		uf.makeSet(v)
		mst.add_vertex(v)
	
	# sort all edges by their weight from lowest to highest
	for e in sorted(G.edges(), key=lambda e:e.weight):
		# if the two end points of the current edge is not in the 
		# same cluster, join them together and add this edge into mst
		if uf.find(e.src) != uf.find(e.dst):
			uf.union(e.src, e.dst)
			mst.add_edge(e.src, e.dst, e.weight)
			print (e.src.info, e.dst.info, e.weight)
	return mst	

def boruvka_mst(G):
	# dict: key=vertex | value=cheapest edge connecting the vertex
	C = dict()
	# union-find data structure
	uf = UnionFind(G.vertices())
	# minimum spanning tree
	mst = UndGraph()
	# add all vertices into mst
	for vert in G.vertices():
		mst.add_vertex(vert)

	# repeat until there is only 1 cluster left
	while (uf.clusters_size()>1):
		# loop all edges 		
		for edge in G.edges():
			src, dst, wei = edge.src,edge.dst,edge.weight
			# find the 2 clusters that,respectively,src 
			# belongs to and dst belongs to
			rootSrc,rootDst = uf.find(src),uf.find(dst)
			
			if rootSrc != rootDst:
				# if they are not in the same cluster and 
				# the cheapest edge of the either cluster
				# is greater than the  weight of the new edge,
				# update the cheapest edge of either cluster
				if not C.get(rootSrc,False) or \
				   C[rootSrc][2] > wei:
					C[rootSrc] = (src,dst,wei)
				if not C.get(rootDst,False) or \
				   C[rootDst][2] > wei:
					C[rootDst] = (src,dst,wei)

		for vert in G.vertices():
			# find a cluster
			if C.get(vert,False):
				src, dst, wei = C[vert]
				rootSrc = uf.find(C[vert][0])
				rootDst = uf.find(C[vert][1])
				if rootSrc != rootDst:
					print (src.info, dst.info, wei)
					mst.add_edge(src,dst,wei)	
					uf.union(rootSrc,rootDst)
		# reset the cheapest cost for clusters since we might merge new
		# clusters
		C.clear()
	
	return mst

if __name__ == "__main__":
	G = UndGraph()
	label = G.read_graph_from_file("../others/hw1.txt")
	mst = prim_jarnik_mst(G, label['A'])
	mst.print_edges()
	print ()
	mst = kruskal_mst(G)
	mst.print_edges()
	print ()
	mst = boruvka_mst(G)
	mst.print_edges()
