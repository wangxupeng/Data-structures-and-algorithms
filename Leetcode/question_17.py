class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        
        d = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        cmbs = [""]
        for num in digits:
            new_combs = []
            for cmb in cmbs:
                for number in d[int(num)]:
                    new_combs.append(cmb + number)
            cmbs = new_combs
        return cmbs
