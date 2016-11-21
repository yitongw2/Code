import utility
import random

if __name__=="__main__":
	test_lis=[random.randint(0,100) for x in range(50)]
	i,k=utility.partition(test_lis,101)
	print (test_lis[50:50])
	print (utility.findMedian(test_lis))
