from __init__ import *
from graph import Graph
from heap import Heap

def dijkstra_shortest_path(G,s):
	# distance: key=vertex ; value=shortest distance from v to key 
	D = dict()
	# distance: key=vertex ; value=parent of the shortest path
	P = dict()
	for v in G.vertices():
		if s == v:
			D[v] = 0
		else:
			D[v] = MAX
	# heap
	Q = Heap(G.vertices(), lambda v:D[v])
	
	while (Q.size()>0):
		v = Q.removeMin()
		for w, wei in G.neighbors(v):
			if D[w] > D[v]+wei:
				D[w] = D[v]+wei
				P[w] = v
				Q.update(w, D[w]) 
	return D,P

def bellman_ford_shortest_path(G,s):
	D = dict()
	P = dict()
	for v in G.vertices():
		if v == s:
			D[v] = 0
		else:
			D[v] = MAX
	
	for v in G.vertices():
		for e in G.edges():
			v, w, wei = e.src, e.dst, e.weight
			if D[w] > D[v]+wei:
				D[w] = D[v]+wei
				P[w] = v
	return D,P
	

if __name__ == "__main__":
	G = Graph()
	label = G.read_graph_from_file("../others/hw1.txt")
	d,p = dijkstra_shortest_path(G,label['A'])
	print ("D")
	for x in d:
		print ("v:",x.info," d:",d[x])
	print ("P")
	for x in p:
		print ("v",x.info," p:",p[x].info)
	print ()
	d,p = bellman_ford_shortest_path(G,label['A'])
	print ("D")
	for x in d:
		print ("v:",x.info," d:",d[x])
	print ("P")
	for x in p:
		print ("v",x.info," p:",p[x].info)
