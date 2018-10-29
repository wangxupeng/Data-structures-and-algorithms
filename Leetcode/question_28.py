class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        point = 0
        
        while m <=n:
            if haystack[point:point+m] == needle:
                return point
            else:
                point +=1
                n-=1
        return -1
            
