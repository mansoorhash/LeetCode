class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        prefix = [s for s in strs[0]]
        for s in strs[1:]:
            t = []
            for i, c in enumerate(s):
                if i > len(prefix) - 1:
                    break

                if c == prefix[i]:
                    t.append(c)
                else:
                    break
            prefix = t
        return ''.join(prefix)
