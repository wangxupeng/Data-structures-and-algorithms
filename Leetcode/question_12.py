#思路是从千位开始减添加对应的字符,当减不了的时候跳到下一个位数再开始减并添加对应字符,以此类推,一直到收敛.
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX","V", "IV", "I"]
        numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        tmp =""
        i = 0
        while i < len(values):
            while num -numbers[i]  >= 0:
                tmp += values[i]
                num -= numbers[i]
            i+=1
        return tmp
