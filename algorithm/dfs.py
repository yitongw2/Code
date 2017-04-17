import __init__
import graph

def dfs(G, v=None):
	if v:
		vl = [v]
	else:
		vl = G._vertices
	htable = dict()
	for x in vl:
		r_dfs(G, x, htable)

def r_dfs(G, v, htable):
	htable[v] = True
	for w,wei in G.neighbors(v):
		if not htable.get(w, False):
			htable[w] = True
			print (v.info, "->", w.info)
			r_dfs(G, w, htable)
			
	
			
if __name__ == "__main__":
	G = graph.Graph()
	labels = G.read_graph_from_file("../others/flights.txt")
	dfs(G, labels['BOS'])
