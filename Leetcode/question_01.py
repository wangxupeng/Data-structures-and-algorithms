#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 17:26
# @Author  : akon_wong
# @File    : 1.py

#way1
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
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
        rest = target - nums[i]
        if rest in set(nums):
            return [i, nums[rest].index]


if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    index_return = twoSum(nums,target)
    print(index_return)
