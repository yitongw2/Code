
def distance(pointX, pointY):
	"""
	for simplicity's sake, only calculates the result without squre root.
	"""
	return (pointX[0]-pointY[0])**2+(pointX[1]-pointY[1])**2

def find_closest_pair(points):
	points.sort(key=lambda x: x[0])
	d=None
	L=points[0]
	R=L
	

if __name__=="__main__":
	points=[(1,3),(2,4),(8,-3),(5,9),(2,2),(0,4)]
	print (find_closest_pair(points))
