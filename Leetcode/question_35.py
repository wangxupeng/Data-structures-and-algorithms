class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        n = len(nums)

        l, r = 0, n - 1

        if target > nums[r]: return r+1
        if target < nums[l] : return 0



        mid = int((l + r) / 2)

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            for i in nums[:mid+1]:
                if i == target:
                    return nums.index(i)

                elif i > target:
                    return nums.index(i)
        else:
            for j in nums[mid-1:]:
                if j == target:
                    return nums.index(j)

                elif j > target:
                    return nums.index(j)
