class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<1: return 
        
        n = len(nums)
        
        idx=0
        for ind in range(n-1,0,-1):
            if nums[ind] > nums[ind-1]:
                idx = ind
                break
                
        if idx !=0:
            for i in range(n-1,idx-1,-1):
                if nums[idx-1]<nums[i]: 
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                    break
        nums[idx:] = nums[idx:][::-1]
