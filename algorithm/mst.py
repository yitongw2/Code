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

if __name__ == "__main__":
	G = UndGraph()
	label = G.read_graph_from_file("../others/num.txt")
	mst = prim_jarnik_mst(G, label['1'])
	mst.print_edges()
	print ()
	mst = kruskal_mst(G)
	mst.print_edges()
