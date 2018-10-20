#数字转化为str:
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) == 0:
            return True
        
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False
            
#数字不转化为str
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or(x!=0 and x%10 ==0):
            return False
        
        half = 0
        while x > half:
            half = half*10 + x%10
            x //= 10
        return x == half or x == half//10
