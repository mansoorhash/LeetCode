class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        v = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in v:
                v[key] = []
            v[key].append(word)

        return list(v.values())