class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or not nums: return [-1,-1]
        
        l,r = 0, len(nums)-1
        
        
        res = []
        while l <= r:
            mid = int((l+r)/2)
            
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                res.append(mid)
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if not res:
            return [-1, -1]
        
        r = len(nums)-1
        
        while l <= r:
            mid = int((l+r)/2)
            
            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target):
                res.append(mid)
                break
                
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 
                
        return res
