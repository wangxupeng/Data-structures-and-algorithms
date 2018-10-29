class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result =[]
        combs = [""]
        
        bracket_n = ["()"]*(n*2)
        
        
        for i in bracket_n:
            new_combs = []
            for cmb in combs:
                for j in i:
                    new_combs.append(cmb+j)
            combs = new_combs
            
        final_list =[]    
        for i in combs:
            if self.isValid(i) == True:
                final_list.append(i)
            
        return final_list
    
    def isValid(self, s):
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        bracket_list = []

        for i in s:
            if i not in d:
                bracket_list.append(i)
            if i in d:
                top = bracket_list.pop() if bracket_list else "@"
                if top != d[i]:
                    return False
        return not bracket_list
