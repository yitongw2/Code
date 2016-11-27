
def lcs_recur(X, Y, i, j):
	"""
	recursive function for computting the longest common sequence of two strings.
	recurrence: if i==0 or j==0: return ""
		    else if X[i-1]==Y[j-1]: lcs_recur(X,Y,i-1,j-1)+X[i-1]
		    otherwise: max(lcs_recur(X,Y,i-1,j), lcs_recur(X,Y,i,j-1))
	"""	
	if i==0 or j==0:
		return ""
	elif X[i-1]==Y[j-1]:
		return lcs_recur(X, Y, i-1, j-1)+X[i-1]
	else:
		stringX=lcs_recur(X, Y, i-1, j)
		stringY=lcs_recur(X, Y, i, j-1)
		if len(stringX)>len(stringY):
			return stringX
		else:
			return stringY

def lcs(X,Y):
	"""
	dynamic programming 
	"""
	table=[]
	for x in range(len(X)+1):
		table.append([0 for y in range(len(Y)+1)])
	for x in range(len(X)+1):
		for y in range(len(Y)+1):
			if x==0 or y==0:
				table[x][y]==0
			elif X[x-1]==Y[y-1]:
				table[x][y]=1+table[x-1][y-1]
			else:
				table[x][y]=max(table[x-1][y], table[x][y-1])
	return table	
	

if __name__=="__main__":
	X="dynamic"
	Y="programming"
	print(lcs_recur(X, Y, len(X), len(Y)))
	for x in lcs(X,Y):
		print (x)
	

