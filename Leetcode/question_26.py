class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0 
        
        pre = 0
        cur = 1
        n = len(nums)
        count = 1
        while pre<cur and cur < n:
            if nums[pre] == nums[cur]:
                cur+=1
            else:
                count+=1
                pre+=1
                nums[pre] = nums[cur]
                cur+=1
        return count
