class Solution:
    def myAtoi(self, s):
        s = s.strip()

        if not s:
            return 0

        sign = 1
        if s[0] in ["-","+"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]
                
        tmp = ""
        for i in s:
            try:
                tmp += str(int(i))
            except:
                break
                           
        if len(tmp) == 0:
            return 0
        else:
            ans = int(tmp) *sign
            
            if ans >= (2**31-1):
                return (2**31-1)
            if ans <= -(2**31):
                return -(2**31
            
            return ans
