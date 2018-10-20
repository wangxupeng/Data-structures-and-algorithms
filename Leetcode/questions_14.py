class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type num: int
        :rtype: str
        """
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        for i in range(len(strs[0])):
            for s in strs:
                if i >= len(s) or strs[0][i] != s[i]:
                    return strs[0][:i] #此处不包含i
                
        return strs[0]

            
