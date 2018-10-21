#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 17:26
# @Author  : akon_wong
# @File    : 1.py

#way1 暴力求解
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            else:
                pass

#way2
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        num = target - nums[i]
        if num in set(nums[i + 1:]):
            return [i, nums[i + 1:].index(num)+i+1]
        else:
            pass
#way3
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d ={}
        
        for i,num in enumerate(nums):
            if num not in d:
                d[target-num] = i
            else:
                return [d[num], i]


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    index_return = twoSum(nums,target)
    print(index_return)
