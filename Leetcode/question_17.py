class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        maps = {2:'abc', 
                3:'def',
                4:'ghi',
                5:'jkl',
                6:'mno',
                7:'pqrs',
                8:'tuv',
                9:'wxyz'
               }
        
        ret_lists = []
        
        def _traverse(cur_str):
            if len(cur_str) == len(digits):
                ret_lists.append(cur_str)
                return
            for char in maps[int(digits[char])]:
                _traverse(cur_str + "{}".format(char))
        _traverse("")
        return ret_lists
