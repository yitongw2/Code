import random
import sorting
import utility


def randomQuickSelect(lis, key):
	"""
	select the ith smallest element in the list using random pivot and partition
	time complexity: O(n) (expected with a pivot of probability of 1/2 --> size of L/G is at most 3n/4)
					 O(n^2)	 (when a bad pivot is choosen --> pivot = the smallest/largest element)
	proof:
			phases/recursive calls : 0,1,2,3 ,..., k
			random variable = X(k) -- the probability that the choosen pivot is a good one (within the middle 50 percent elements)
			size of elements at each phase/recursive call with the probability of X(k) : X(k)*n*(3/4)^k
			work done for each phase : c*X(k)*n*(3/4)^k                                           
			work done until phase k : c*X(0)*n*(3/4)^0+c*X(1)*n*(3/4)^1+...+c*X(k)*n*(3/4)^k --> ∑[k=0->k=log(4/3)n](cnX(k)(3/4)^k)
			avergae case : E( ∑[k=0->k=log(4/3)n](cnX(k)(3/4)^k) ) --> cnE( ∑[K=0->K=log(4/3)n](X(k)(3/4)^k)) --> cn∑[K=0->K=log(4/3)n](E(X(k)(3/4)^k))
																															   ||
																															   ||
																															   \/
														   2cn ∑[K=0->K=log(4/3)n]((3/4)^k)	<-- cn ∑[K=0->K=log(4/3)n](2(3/4)^k) <-- cn ∑[K=0->K=log(4/3)n](E(X(k))(3/4)^k )

														   Since ∑[K=0->K=log(4/3)n]((3/4)^k) -- geomertric series <=1

														   Therefore, 2cn ∑[K=0->K=log(4/3)n]((3/4)^k) --> O(2cn) --> O(n)


	memory space: O(n)  
	"""
	if len(lis)==1:
		return lis[0]
	else:
		pivotI=random.randint(0,len(lis)-1)
		i,k=utility.partition(lis,lis[pivotI]) 
		if key<=i:
			return randomQuickSelect(lis[:i],key)
		elif key<=i+len(lis)-k:
			return lis[k]
		else:
			return randomQuickSelect(lis[i:k],key-i-len(lis)+k)
	

def deterQuickSelect(lis,key):
	if len(lis)==1:
		return lis[0]
	else:
		g=len(lis)/5
		subM=[utility.findMedian(lis[x*5:(x+1)*5]) for x in range(g)]
		if len(lis)%5!=0:
			subM.append(utility.findMedian(lis[g*5:]))
		m=deterQuickSelect(subM,g/2 if g%2==0 else g/2+1)
		i,k=utility.partition(lis,m)
		if key<=i:
			return deterQuickSelect(lis[:i],key)
		elif key<=i+len(lis)-k:
			return lis[k]
		else:
			return deterQuickSelect(lis[i:k],key-i-len(lis)+k)	
		
			


'''
if __name__=="__main__":
	SIZE=100
	RANGE=50

	#ii=utility.partition(test_lis,RANGE-1)
	#print (test_lis)
	#print (ii)
	#print (utility.isPartitioned(test_lis,test_lis[ii[1]],ii[0]))

	for y in range(50):
		test_lis=[random.randint(0,SIZE) for x in range(RANGE)]
		l=[]
		for r in range(RANGE):	
			l.append(deterQuickSelect(test_lis,r+1))
		sorting.quickSort(test_lis,0,RANGE-1)
		print ("RESULT",test_lis==l)
'''
