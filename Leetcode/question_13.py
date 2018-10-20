#从前往后扫描，用一个临时变量记录分段数字。
#如果当前比前一个大，说明这一段的值应当是这个值减去上一个值。比如IV = 5-1 =4;
#否则，将当前值加入到结果中，然后开始下一段记录，比如VI = 5 + 1, II = 1 +1

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"M":1000, "D":500, "C":100, "L":50, "X":10,"V":5, "I":1}
        ans = 0
        for i in range(len(s)):
            if i>0 and  values[s[i]] > values[s[i-1]]:
                ans += values[s[i]] - 2*values[s[i-1]]
            else:
                ans += values[s[i]]
        return ans
