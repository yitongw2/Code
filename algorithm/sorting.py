import random

def insertionSort(lis):
	for i in range(len(lis)):
		k=i
		for j in reversed(range(i)):
			if lis[j]>lis[k]:
				temp=lis[k]
				lis[k]=lis[j]
				lis[j]=temp
				k=j		

def selectionSort(lis):
	for x in reversed(range(len(lis))):
		ma=x
		for y in range(x):
			if lis[y]>lis[ma]:
				ma=y
		temp=lis[ma]
		lis[ma]=lis[x]
		lis[x]=temp

def treeSort(lis):
	"not in-place"
	return lis

def heapSort(lis):
	"not in-place"
	return lis

def quickSort(lis,low,high):
	if high-low<1:
		pass
	else:
		pivot=lis[high]
		i=0
		j=high-1
		while (i<=j):
			if lis[i]>pivot:
				if lis[j]<=pivot:
					temp=lis[i]
					lis[i]=lis[j]
					lis[j]=temp
					i+=1	
				j-=1
			else:
				i+=1
		lis[high]=lis[i]
		lis[i]=pivot
		quickSort(lis,0,i-1)
		quickSort(lis,i,high)
			
def mergeSort(lis):  # how many recursive calls = 1+2+4+...+n
	if len(lis)<2:
		return lis   
	else:
		mid=int(len(lis)/2) 
		left=mergeSort(lis[:mid])
		right=mergeSort(lis[mid:])
		emp=[0]*(len(left)+len(right))
		#----------------merge-----------------
		i,j=0,0
		for x in range(len(emp)):   #    n 
			if j>=len(right):
				emp[x]=left[i]
				i+=1
			elif i>=len(left):
				emp[x]=right[j]
				j+=1
			elif left[i]<=right[j]:
				emp[x]=left[i]
				i+=1
			elif right[j]<left[i]:
				emp[x]=right[j]
				j+=1
			else:
				pass
		#----------------merge-----------------
		return emp

def bucketSort(lis):
	if len(lis)<2:
		return lis
	max=lis[0]
	for x in lis:
		if x>max:
			max=x
	buck=[0]*(max+1)
	for x in lis:
		buck[x]+=1
	result=[]
	inde=0
	for x in buck:
		for y in range(x):
			result.append(inde)
		inde+=1	
	return result
		
	
		
	
			

'''

if __name__=="__main__":
	for y in range(100):
		test_lis=[random.randint(0,100) for x in range(50)]
		sl=sorted(test_lis)
		quickSort(test_lis,0,len(test_lis)-1)
		print (sl==test_lis)
'''
