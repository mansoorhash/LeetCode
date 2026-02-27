class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]
        last = strs[-1]
        r = ""
        for i in range(min(len(prefix),len(last))):
            if prefix[i] != last[i]:
                return r
            r += prefix[i]
        return r