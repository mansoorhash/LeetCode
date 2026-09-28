class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0
        l = 0
        for i, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            result = max(result, i-l+1)
        return result 


        
