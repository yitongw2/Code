
class Vertex:
	def __init__(self, info=None, v_num=-1):
		self.info = info
		self.v_num = v_num
		
class Edge:
	def __init__(self, src, dst, weight=0):
		self.src = src
		self.dst = dst
		self.weight = weight

class Graph:
	def __init__(self):
		self._vertices = []
		self._edges = []
	
	def add_vertex(self, vert):
		# O(1) time
		if not self.vertex_in_graph(vert):
			vert.v_num = len(self._vertices)
			self._vertices.append(vert)
			self._edges.append([])
	
	def add_edge(self, src, dst, weight=0, info=None):
		# O(1) time 
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			self._edges[src.v_num].append(Edge(src, dst, weight))
	
	def remove_vertex(self, vert):
		# 
		if self.vertex_in_graph(vert):
			# O(1)
			self._vertices[vert.v_num] = None
			self._edges[vert.v_num] = []
			# O(|E|) for checking and removing all edges that
			# involves vertex vert
			for src in self._vertices:
				self.remove_edge(src, vert)
			vert.v_num = -1
	
	def remove_edge(self, src, dst):
		# O(|V|) since each vertex can only have at most |V| vertices
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			for edge in self._edges[src.v_num]:
				if edge.dst == dst:
					self._edges[src.v_num].remove(edge)						
	def adjacent(self, src, dst):
		# O(|V|)
		if self.vertex_in_graph(src) and self.vertex_in_graph(dst):
			for edge in self._edges[src.v_num]:
				if edge.dst == dst:
					return True
		return False
	
	def neighbors(self, src):
		# O(1)
		if self.vertex_in_graph(src):
			return [(x.dst, x.weight) for x in self._edges[src.v_num]]	
	
	def vertex_in_graph(self, vert):
		# O(1)
		return vert and 0<=vert.v_num<len(self._vertices) and \
		       self._vertices[vert.v_num]
	
	def reverse_graph(self):
		new_g = Graph()
		new_g._vertices = self._vertices
		for vert in self._vertices:
			new_g._edges.append([])
		for edge in self._edges:
			for e in edge:
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
				self.add_edge(dic[l[0]], dic[l[1]], l[2])
		return dic
	
	def print_vertices(self):
		for v in self._vertices:
			print (v.info, v.v_num)

	def print_edges(self):
		for edges in self._edges:
			for edge in edges:
				print (edge.src.info, edge.dst.info, edge.weight)
	
if __name__ == "__main__":
	G = Graph()
	label = G.read_graph_from_file("../others/seattle_map.txt")
	G.remove_edge(label['50'], label['40th&148th'])
	print (label)
	#G.print_vertices()
	G.print_edges()
	print (G.adjacent(label['27'], label['24th&148th']))
	ng = G.reverse_graph()
	ng.print_edges()
