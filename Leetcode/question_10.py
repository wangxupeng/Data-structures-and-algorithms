#暴力法
def isPalindrome(height):
    """
    :type height: List[int]
    :rtype: int
    """
    tmp = 0
    for i, num in enumerate(height):
        for j, sec_num in enumerate(height[i + 1:]):
            h = min(num, sec_num)
            l = j + 1
            area = l * h
            if area > tmp:
                tmp = area
    return tmp
    


#双指针法
算法

这种方法背后的思路在于，两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。

我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。 此外，我们会使用变量 maxareamaxarea 来持续存储到目前为止所获得的最大面积。 在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxareamaxarea，并将指向较短线段的指针向较长线段那端移动一步。
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        
        maxarea = 0
        while start<end:
            area = min(height[start],height[end]) * (end-start)
            if area > maxarea:
                maxarea = area
            if height[start] > height[end]:
                end -= 1
            else:
                start+=1
        return maxarea
