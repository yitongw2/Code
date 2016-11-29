
class Item:
	def __init__(self, name, size, value):
		self.name=name
		self.size=size
		self.value=value

def fractional_knapsack(items, limit):
	"""
	greedy approach.
	idea: select as much as the item with the largest value per size until the
	      knapsack is filled up.
	steps:
	      1, sort the items by value per size
	      2, loop through items and fill up as much as valuable item per size
	      3, when limit is reached, done  
	
	"""
	result=[]
	remaining_space=limit
	items.sort(key=lambda x: -x.value/float(x.size))
	for item in items:
		if remaining_space<=0:
			break	
		amount=min(item.size, remaining_space)
		fraction=amount/float(item.size)
		result.append(Item(item.name, amount, item.value*fraction))
		remaining_space-=amount
	return result


def zero_one_knapsack(items, L):
	"""
	recurrence formula:
		if no item to be selected or knapsack is full, 
			no items could be included.
		else if still have space for an particular item i:
			choose the better solution between to include the item
			or not to include the item. 
	"""
	table=[]
	for i in range(len(items)+1):
		table.append([0 for s in range(L+1)])
	for i in range(len(items)+1):
		for s in range(L+1):
			if i==0 or s==0:
				table[i][s]=0
			elif s>=items[i-1].size:
				table[i][s]=\
				max(items[i-1].value+table[i-1][s-items[i-1].size],\
				table[i-1][s])
	return table

def traceBack(items, L, table):
	"""
	trace back along the table.
	if the table cell above it is the same, the item at i,j is not included.	else, the item is included, go to cell and decrement s by the size of 
	item.
	at last, decrement i by 1. 
	"""
	i=len(items)
	s=L
	output=[]
	while (i!=0 or s!=0):
		lastItem=table[i-1][s]
		if lastItem!=table[i][s]:
			output.append(items[i-1])
			s-=items[i-1].size
		i-=1
	return output
	
				
		

if __name__=="__main__":
	items=[Item("A",3,2),Item("B",4,2),Item("C",10,27), Item("D",6,4),\
			Item("E",9,1),Item("F",8,6), Item("G",5,12)]
	limit=15
	print ("Items: ", [(x.name,x.size,x.value) for x in items])
	print ("Limit: ", limit)
	print ("*********************")
	print ("Fractional Knapsack: ")
	result=fractional_knapsack(items, 15)
	print ("Selected Items (greedy approach): ",[(x.name, x.size, x.value) for x in result]) 
	print ("Max Value: ", sum([x.value for x in result]))
	print ("*********************")
	print ("0-1 Knapsack")
	result=zero_one_knapsack(items, limit)
	print ("Dynamic Programming table:")
	for x in result:
		print (x)
	print ("Selected Items: ", [(x.name,x.size,x.value) for x in traceBack(items, limit, result)])
