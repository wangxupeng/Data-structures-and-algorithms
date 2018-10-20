class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num1_point,num2_point = 0,0
        new = []
        while num1_point <len(nums1) and num2_point<len(nums2):
            if nums1[num1_point] >= nums2[num2_point]:
                new.append(nums2[num2_point])
                num2_point += 1
            else:
                new.append(nums1[num1_point])
                num1_point += 1
        new += nums1[num1_point:]
        new += nums2[num2_point:]
        half = len(new)//2
        return (new[half]+new[~half])/2
                       
# 主要思路是先排序,如果是偶数序列就是中间的两个数之和除以二,如果是奇数序列就是中间的数,这里用了反数的概念
'''
对 return (data[half] + data[~half]) / 2 的解释：

排序后得到序列[1,2,3,4,5,6]，其列表长度为偶数，中位数由列表中间两位元素3（索引为2）,4（索引为3）决定。而元素4的负索引为-3，正好是索引2的取反数。

排序后得到序列[1,2,3,4,5]，其列表长度为奇数，中位数由列表中间元素3（索引为2，负索引为-3）决定。仍然符合代码。
'''
