
# Leetcode 463

def getPerimeter(grid, row_i, col_i):
	p=0
	if row_i-1<0 or grid[row_i-1][col_i]!=1:
		p+=1
	if row_i+1>=len(grid) or grid[row_i+1][col_i]!=1:
		p+=1
	if col_i-1<0 or grid[row_i][col_i-1]!=1:
		p+=1
	if col_i+1>=len(grid[row_i]) or grid[row_i][col_i+1]!=1:
		p+=1
	return p

def islandPerimeter(grid):
	# time complexity : O(row x col)
	p=0
	for row_i in range(len(grid)):
		for col_i in range(len(grid[row_i])):
			if grid[row_i][col_i]==1:
				p+=getPerimeter(grid, row_i, col_i)
	return p

if __name__=="__main__":
	grid=[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
	print (islandPerimeter(grid))