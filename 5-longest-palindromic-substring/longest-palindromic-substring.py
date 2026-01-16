class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
        if len(s) == 2 and s[0] == s[1]: return s
        
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1
            return s[left + 1:right]
            
        longest = s[0]

        for i in range(len(s)):
            odd = expand_from_center(i, i)
            if len(odd) > len(longest):
                longest = odd

            if i + 1 < len(s):
                even = expand_from_center(i, i + 1)
                if len(even) > len(longest):
                    longest = even
        return longest