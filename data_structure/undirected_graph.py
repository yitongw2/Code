from graph import Graph, Edge

class UndGraph(Graph):
	def __init__(self):
		super().__init__()
	
	def add_edge(self, src, dst, weight=0, info=None):
		# O(1) time
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			self._edges[src.v_num].append(Edge(src, dst, weight))
			self._edges[dst.v_num].append(Edge(dst, src, weight))
	
	def remove_edge(self, src, dst):
		super().remove_edge(src, dst)
		super().remove_edge(dst, src)

if __name__ == "__main__":
	G = Graph()
	label = G.read_graph_from_file("../others/seattle_map.txt")
	G.remove_edge(label['50'], label['40th&148th'])
	print (label)
	G.print_vertices()
	G.print_edges()
	print (G.adjacent(label['27'], label['24th&148th']))
