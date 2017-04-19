import __init__
from graph import Graph, Vertex
from stack import Stack

def r_dfs(G, v, htable, action=lambda x: None):
	htable[v] = True
	for w,wei in G.neighbors(v):
		if not htable.get(w, False):
			htable[w] = True
			r_dfs(G, w, htable, action)
	action(v)	

def kosaraju_scc(G):
	# intuition : if u can reach v, v should be able to reach u. 
	result = []
	htable = dict()
	st = Stack()
	for v in G.vertices():
		if not htable.get(v, False):
			r_dfs(G, v, htable, lambda x:st.push(x))
	# try on reversed graph
	htable.clear()
	rG = G.reverse_graph()
	while (st.size()>0):
		root = st.pop()
		if not htable.get(root, False):
			comp = []
			r_dfs(rG, root, htable, lambda x:comp.append(x))
			result.append(comp)
	return result	

def tar_dfs(G, v, htable, index, st, result):
	# visit v first, so push v onto stack
	st.push(v)
	
	# mark it as [index, index, True]
	# now, v has depth of index, can be reached from at least itself and
	# is already visited
	htable[v] = [index, index, True]
	
	# go to v's neighbors
	for w, wei in G.neighbors(v):

		# if w is not visited
		if not htable.get(w, False):
			
			# recurse on w
			tar_dfs(G, w, htable, index+1, st, result)
			
			# by transitivity, if w has a smaller lowlink,
			# update the lowlink
			htable[v][1] = min(htable[v][1], htable[w][1])
		
		elif htable[w][2]:
			# if w is already visited and w is still on stack
			# it means we have found a cycle that not yet being
			# marked, update the lowlink of v if v can be reached 
			# from w and w is positioned earlier in dfs-tree that 
			# the current v's lowlink 
			htable[v][1] = min(htable[v][1], htable[w][0])

	if htable[v][0] == htable[v][1]:
		# if index == lowlink, the root of a scc because it can be
		# reached from the lowest link of itself
		comp = []
		while (st.size()>0):
			root = st.pop()
			htable[root][2] = False
			comp.append(root)
			if root == v:
				break
		result.append(comp)


def tarjan_scc(G):
	# keep track of a vertex's depth in the dfs-tree 
	index = 0
	# hold important info for vertices;
	# key Vertex object 
	# a vertex info(value) [index:int, lowlink:int, visited:boolean]
	htable = dict()
	# store the order that dfs visits
	st = Stack()
	# store scc in result
	result = []
	for v in G.vertices():
		if not htable.get(v, False):
			tar_dfs(G, v, htable, index, st, result)
	return result

if __name__ == "__main__":
	G = Graph()
	labels = G.read_graph_from_file("../others/num.txt")
	print ("Tarjan")
	for sets in tarjan_scc(G):
		print ([x.info for x in sets])
	print ("Kosaraju")
	for sets in kosaraju_scc(G):
		print ([x.info for x in sets])
