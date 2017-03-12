import selecting

def merge2(nums1, m, nums2, n):
	for x in range(n):
		nums1.append(None)
	
	i,j,k = m-1, n-1, m+n-1
	while (i>=0 and j>=0):
		if nums1[i]>=nums2[j]:
			nums1[k] = nums1[i]
			i-=1
		else:
			nums1[k] = nums2[j]
			j-=1


def mergeKLists(lists):
	window=[]
	console=[0]*len(lists)




if __name__=="__main__":
	mergeKLists([])
