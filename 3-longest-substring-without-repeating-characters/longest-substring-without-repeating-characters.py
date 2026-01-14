class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = []
        temp = []
        for c in s:
            if c not in temp:
                temp.append(c)
            else:
                for i,j in enumerate(temp):
                    if j == c:
                        t = temp[i+1:]
                temp = t
                temp.append(c)
            if len(temp) > len(longest):
                longest = temp
        return len(longest)