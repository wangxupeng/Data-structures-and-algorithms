#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 22:45
# @Author  : akon_wong
# @File    : 16.py

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3:
            return sum(nums)

        d = {}
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] - target > 0:
                    d[nums[i] + nums[l] + nums[r]] = abs(nums[i] + nums[l] + nums[r] - target)
                    r -= 1

                elif nums[i] + nums[l] + nums[r] - target < 0:
                    d[nums[i] + nums[l] + nums[r]] = abs(nums[i] + nums[l] + nums[r] - target)
                    l += 1
                else:
                    return nums[i] + nums[l] + nums[r]
        return min(d, key=d.get)
