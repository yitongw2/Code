

def extractSubMatrix(matrix, col):
	subMatrix=[]
	for i in range(1, len(matrix)):
		subMatrix.append([matrix[i][j] for j in range(len(matrix[i]))\
				if j!=col])
	return subMatrix
				



def getDeterminants(matrix):
	"""
	recursive algorithm to calculate the determinant of a matix.
	base case: 2X2 matrix 
		   e.g.  [a, b] -->
			 [c, d] --> formula = a*d-b*c
	recursive case: nXn matrix 
			[a, b, c]
			[d, e, f]
			[g, h, i]
		return a*recursive calll on [e, f]
					    [h, i]
		       -
		       b*recursive call on [d, f]
					   [g, i]
		       +
			c*recursive call on [d, e]
					    [g, h]
	"""
	if len(matrix)==2 and len(matrix[0])==2:
		return matrix[0][0]*matrix[1][1]-\
			matrix[0][1]*matrix[1][0]
	else:
		result=0
		for col in range(len(matrix[0])):
			coefficient=matrix[0][col]
			if (col+1)%2==0:
				coefficient=0-coefficient
			result+=coefficient*\
				getDeterminants(extractSubMatrix(matrix, col))
		return result		
		



if __name__=="__main__":
	print (getDeterminants([[1,3,2],[4,1,3],[2,5,2]]))
