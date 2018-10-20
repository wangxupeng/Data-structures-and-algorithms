class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s
        if s == s[::-1]:
            return s
        else:
            d = {}
            for i in range(len(s)):
                for j in range(i + 1, len(s)+1):
                    a = s[i:j]
                    if a == a[::-1]:
                        d[a] = len(a)
            if d:
                return max(d, key=d.get)
            else:
                return s[0]
#贪心算法
