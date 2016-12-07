
class Node:
        def __init__(self, value, left, right):
                self.left=left
                self.right=right
                self.val=value

class dNode(Node):
	def __init__(self, val, left, right, depth=0):
		Node.__init__(self, val, left, right)
		self.depth=depth

