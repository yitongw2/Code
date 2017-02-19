
def setUpTable(size):
	# set up a square (size x size) table for dynamic programming
	# initially, every cell in None
	table=[]	
	for x in range(size):
		table.append([None for y in range(size)])
	return table

def printTable(table):
	# print out the table in a formatted way (row by col) 
	for row in table:
		print (row) 

def allCombos(table, row, col):
	# given a pair of coordinate (row, col) in the table, computed all combinations
	# possible according to rule Xij={Xik Xk+j | i<=k<j}. Ex, X12 = X11 X22
	# and X11=AC and X22=B, all possible combinations for X12 = {AB, CB}
	result=[]
	for x in range(row, col):
		for r in table[row][x]:
			for c in table[x+1][col]:
				result.append(r+c)	
	return result

def find(table, prod, tar, t=False):
	# find the productions that have tar as their possible combinations
	result=set()
	# if it is not the base case (specified by t)
	if not t:
		# compute all possible combinations
		row, col=tar
		combos=allCombos(table, row, col)
	# loop through each productions
	for rule in prod:
		# if base case and production is nonterminal to terminal and 
		# terminal is tar
		if t and len(rule[1])==1 and rule[1]==tar:
			# add the left-hand of production to result
			result|={rule[0]}
		elif not t and len(rule[1])==2 and rule[1] in combos:
			result|={rule[0]}					
	return result if result!="" else None

def stringInLanguage(prod, startSymbol, string):
	"""
	this function calls cyk() algorithm to compute the dynamic programing table. To determine whether the given string is in the language, which must be in Chomsky Normal Form, simply check whether the start symbol is in the the top-right cell of the table. 
	"""
	return startSymbol in cyk(prod, string)[0][-1] 

def cyk(prod, string):
	# set up empty table
	table=setUpTable(len(string))
	# set up diagonal init value
	for x in range(len(string)):
		table[x][x]="".join(find(table, prod, string[x], t=True))
	for col in range(1,len(string)):
		for row in range(len(string)-col):
			table[row][row+col]="".join(find(table, prod, (row, row+col)))
	return table

if __name__=="__main__":
	prod=(["S", "AB"], ["S", "BC"], ["A", "BA"], ["A", "a"], ["B", "CC"], ["B","b"], ["C","AB"], ["C", "a"])
	print(stringInLanguage(prod, "S", "baaab"))	
