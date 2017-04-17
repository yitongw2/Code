import __init__
import graph

def bfs(G, v):
	htable = dict()
	queue = [v]
	htable[v] = True
	while (len(queue)>0):
		vert = queue.pop(0)
		print (vert.info)
		for w, wei in G.neighbors(vert):
			if not htable.get(w, False):
				htable[w] = True
				queue.append(w)
		

if __name__ == "__main__":
	G = graph.Graph()
	labels = G.read_graph_from_file("../others/flights.txt")
	bfs(G, labels['BOS'])
