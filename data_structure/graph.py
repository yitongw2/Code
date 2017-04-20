class Vertex:
	def __init__(self, info=None, v_num=-1):
		self.info = info
		
class Edge:
	def __init__(self, src, dst, weight=0):
		self.src = src
		self.dst = dst
		self.weight = weight

class Graph:
	def __init__(self):
		self._adj_list = dict()
	
	def add_vertex(self, vert):
		# O(1) time
		if not self.vertex_in_graph(vert):
			self._adj_list[vert] = []
	
	def add_edge(self, src, dst, weight=0, info=None):
		# O(1) time 
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			self._adj_list[src].append(Edge(src, dst, weight))
	
	def remove_vertex(self, vert):
		# 
		if self.vertex_in_graph(vert):
			# O(|E|) for checking and removing all edges that
			# involves vertex vert
			for src in self._adj_list:
				self.remove_edge(src, vert)
			del self._adj_list[vert]
	
	def remove_edge(self, src, dst):
		# O(|V|) since each vertex can only have at most |V| vertices
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			for edge in self._adj_list[src]:
				if edge.dst == dst:
					self._adj_list[src].remove(edge)						
	def adjacent(self, src, dst):
		# O(|V|)
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			for edge in self._adj_list[src]:
				if edge.dst == dst:
					return True
		return False
	
	def neighbors(self, src):
		# O(1)
		if self.vertex_in_graph(src):
			return [(x.dst, x.weight) for x in self._adj_list[src]]	
	
	def vertex_in_graph(self, vert):
		# O(1)
		return self._adj_list.get(vert, None)!=None
	
	def reverse_graph(self):
		new_g = Graph()
		for vert in self._adj_list:
			new_g.add_vertex(vert)		
		for edges in self._adj_list.values():
			for e in edges:
				new_g.add_edge(e.dst,e.src,e.weight)	
		return new_g
		

	def read_graph_from_file(self, fname):
		dic = dict()
		with open(fname, "r") as f:
			vn = int(f.readline())
			for v in range(vn):
				info = f.readline().strip()
				dic[info] = Vertex(info)
				self.add_vertex(dic[info])
			en = int(f.readline())
			for e in range(en):
				l = f.readline().strip().split()
				self.add_edge(dic[l[0]], dic[l[1]], int(l[2]))
		return dic
	
	def vertices(self):
		return [x for x in self._adj_list]
	
	def edges(self):
		result = []
		for edges in self._adj_list.values():
			result.extend([edge for edge in edges])
		return result

	def print_vertices(self):
		print ("Vertices:")
		for v in self._adj_list:
			print (v.info)

	def print_edges(self):
		print ("Edges:")
		for edges in self._adj_list.values():
			for edge in edges:
				print (edge.src.info, edge.dst.info, edge.weight)



class UndGraph(Graph):
	def __init__(self):
		super().__init__()
	
	def add_edge(self, src, dst, weight=0, info=None):
		# O(1) time
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			super().add_edge(src, dst, weight)
			super().add_edge(dst, src, weight)
	
	def remove_edge(self, src, dst):
		super().remove_edge(src, dst)
		super().remove_edge(dst, src)		
	

if __name__ == "__main__":
	G = Graph()
	label = G.read_graph_from_file("../others/seattle_map.txt")
	G.remove_vertex(label['40th&148th'])
	print (label)
	G.print_vertices()
	G.print_edges()
	print (G.adjacent(label['27'], label['24th&148th']))
	ng = G.reverse_graph()
	ng.print_vertices()
	ng.print_edges()
