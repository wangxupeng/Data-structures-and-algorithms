class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        s = s[::-1]
        s = s.strip()
        if " " in s:
            return s.index(" ")
        if " " not in s:
            return len(s)
