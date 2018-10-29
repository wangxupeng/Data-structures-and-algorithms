class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0: return 0
        
        
        pre = 0
        cur = 0
        n = len(nums)
        count = 0
        while pre<=cur  and cur <n:
            if nums[cur] == val:
                cur+=1
            else:
                count+=1

                nums[pre] = nums[cur]
                pre+=1
                cur+=1
        return count
