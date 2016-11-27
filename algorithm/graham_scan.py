import random
import stack
import matrix_determinant

class Point:
	def __init__(self, x, y):
		self.x=x
		self.y=y

def makeMatrix(*points):
	"""
	create a 2D list representing an nx3 matrix given all
	points. 
	"""
	matrix=[]
	for p in points:
		matrix.append([p.x, p.y, 1])
	return matrix

def grahamScan(points):
	"""
	Graham Scan:
		1, sort all points by their x coordinate (if tie occurs, choose the 
		   point with the larger y corrdinate)
		2, initialize an empty Stack
		3, loop through those sorted points. 
		4, for each looped point, 
			while the last two points in stack forms a left turn (matrix dete			 rminant>0) with the point, pop the last point in stack.
		   at the end of the loop, push the point into the stack
		5, return the stack (remaining points in stack)
	"""
	
	# sort points by x coordinate (if tie occurs, choose the larger y)
	points.sort(key=lambda point:(point.x, -point.y))
	
	# initialize an empty stack
	s=stack.Stack()
	
	for point in points:
		if s.size()<2:
			s.push(point)
		else:
			while (s.size()>1):
				q=s.pop()
				p=s.top()
				matrix=makeMatrix(p, q, point)
				if matrix_determinant.getDeterminants(matrix)<=0:
					s.push(q)
					break
			s.push(point)								
	return s	
			

if __name__=="__main__":
	l=[Point(1,3), Point(5,2), Point(3,4), Point(4,5), \
		Point(6,3), Point(2,0), Point(2,3), Point(4,1)]
	s=grahamScan(l);
	print ("Graph:", [(p.x, p.y) for p in l])
	print ("Upper Half of the Convex Hull:",[(p.x, p.y) for p in s.arr])
