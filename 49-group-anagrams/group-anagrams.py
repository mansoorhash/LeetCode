class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        v = {
            "".join(sorted(word)): []
            for word in strs
            }
        for word in strs:
            v["".join(sorted(word))].append(word)
        result = []
        for item in v.values():
            result.append(item)
        return result