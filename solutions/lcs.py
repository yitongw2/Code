
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
		return X[i-1]+lcs_recur(X, Y, i-1, j-1)
	else:
		stringX=lcs_recur(X, Y, i-1, j)
		stringY=lcs_recur(X, Y, i, j-1)
		if len(stringX)>=len(stringY):
			return stringX
		else:
			return stringY

def lcs(X,Y):
	"""
	dynamic programming 
	use memoization --> build a 2D list for storage
	recurrence formula: 
		if x==0 or y==0: set table cell at (x, y) to 0 // one of the string has 0 length, no common char
		elif X[x-1]==Y[y-1]: increment table cell at (x-1, y-1) with 1
		else: choose the max value between table cell (x-1, y) and (x, y-1)
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

def traceBack(X, Y, table):
	"""
	Given a dynamic programming table, trace back the actual common substring of 
	X and Y.
	"""
	i=len(X)
	j=len(Y)
	result=[]
	while (i+j>0):
		if X[i-1]==Y[j-1]:
			result.append(X[i-1])
			i-=1
			j-=1
		else:
			if table[i-1][j]>table[i][j-1]:
				i-=1
			else:
				j-=1
	return "".join(reversed(result))	
		

if __name__=="__main__":
	X="dynamic"
	Y="programming"
	print ("X=", X, "Y=", Y)
	#print("LCS(recursive)=", lcs_recur(X, Y, len(X), len(Y)))
	table=lcs(X,Y)
	print ("LCS(dynamic programming table)")
	for x in table:
		print (x)
	print ("result=", traceBack(X,Y,table))
		

