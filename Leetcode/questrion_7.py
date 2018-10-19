class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        final = -int(str(abs(x))[::-1]) if x < 0 else int(str(x)[::-1])
        x = 0 if abs(final) > 0x7FFFFFFF else final
        return x
        
# 举一反三题目 I am a student. 反转


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    word_list = []
    word = ""
    for i, c in enumerate(x):
        if c != " " and i != len(x)-1:
            word += c
        else:
            if c !=" ":
                word+=c
            word_list.insert(0, word)
            word = ""
    return " ".join(word_list)


if __name__ == '__main__':
    s = "i am a student."
    a = reverse(s)
    print(a)
