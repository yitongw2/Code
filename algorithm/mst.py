import __init__
from graph import UndGraph, Vertex, Edge
from heap import Heap


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
		for w,wei in G.neighbors(v):
			if w in pq.arr and C[w]>wei:
				C[w] = wei
				E[w] = (v,wei)
				pq.update(w,wei)
	
	return mst


if __name__ == "__main__":
	G = UndGraph()
	label = G.read_graph_from_file("../others/num.txt")
	mst = prim_jarnik_mst(G, label['1'])
	mst.print_edges()
		
