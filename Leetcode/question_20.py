class Solution(object):
    def isValid(self, s):
        stack = []
        d = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for i in s:

            if i in d:
                top_element = stack.pop() if stack else "@"

                if d[i] != top_element:
                    return False

            else: stack.append(i)

        if len(stack) == 0:
            return True
        if len(stack) > 0:
            return False
