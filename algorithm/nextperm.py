
def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # k = the index before the longest non-increasing sequence
        k = -1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                k = i-1
        if k<0:
            nums.reverse()
            return
        # find the largest l that l>=k+1 and nums[l]>nums[k]
        l = k+1
        for j in range(l, len(nums)):
            if nums[j] > nums[k]:
                l = j
        # swap nums[l] and nums[k]
        tmp = nums[l]
        nums[l] = nums[k]
        nums[k] = tmp
        
        # treat the suffix as a separate array starts with nums[base] to nums[-1] and reverse it. 
        # it is to restore the ordering of suffix to the lowest permutation possible. 
        base = k+1
        size = len(nums)-base
        for x in range(size/2):
            tmp = nums[x+base]
            nums[x+base] = nums[size-1-x+base]
            nums[size-1-x+base] = tmp
        
