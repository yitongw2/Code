
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

if __name__=="__main__":
	items=[Item("A",3,3),Item("B",4,2),Item("C",10,27), Item("D",6,4),\
			Item("E",9,1),Item("F",8,6), Item("G",5,12)]
	limit=15
	print ("Items: ", [(x.name,x.size,x.value) for x in items])
	print ("Limit: ", limit)
	print ("*********************")
	print ("Fractional Knapsack: ")
	result=fractional_knapsack(items, 15)
	print ("Greedy Approach: ",[(x.name, x.size, x.value) for x in result]) 
	print ("Max Value: ", sum([x.value for x in result]))
