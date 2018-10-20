class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        else:
            ans =""
            i = 0
            point =0
            while i <= (numRows -1):
                if i == 0:
                    try:
                        ans += s[point*(2* numRows -2)]
                        point += 1
                    except:
                        i+=1
                        point = 0
                if i == (numRows -1):
                    try:
                        ans += s[point*(2* numRows -2)+numRows -1]
                        point += 1
                    except:
                        break
                if i!=0 and i !=(numRows -1) :
                    try:
                        ans += s[point*(2* numRows -2)+i]
                        ans += s[(point+1)*(2* numRows -2)-i]
                        point += 1
                    except:
                        i+=1
                        point = 0
            return ans
            
#找每行的规律,然后再把规律写成代码,很符合我这种学数学的,try函数比while快,就酱.
