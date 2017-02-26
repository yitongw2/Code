
def findDisappearedNums(nums):
	result=[]
	for x in nums:
		num=abs(x)-1
		if nums[num]>0:
			nums[num]=(-nums[num])
	for i in range(len(nums)):
		if nums[i]>0:
			result.append(i+1)
	return result

if __name__=="__main__":
	nums=[4,3,2,7,8,2,3,1]
	print (findDisappearedNums(nums))
