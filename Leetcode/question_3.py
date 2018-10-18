def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
        if c in d:
            start = max(start, d[c] + 1)
        d[c] = i
        ans = max(ans, i - start + 1)
    return ans

#举一反三 返回最大子字符串
def returnOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    d ={}
    for i in range(len(s)):
        tmp = s[i]
        for j in s[i+1:]:
            if j not in tmp:
                tmp+=j
            else:
                d[tmp]=len(tmp)
                break
    return max(d,key=d.get)
    
if __name__ == '__main__':
    s =     "pwwkew"
    a = lengthOfLongestSubstring(s)
    print(a)
