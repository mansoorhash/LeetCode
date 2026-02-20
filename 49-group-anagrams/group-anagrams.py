class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        v = defaultdict(list)
        for word in strs:
            letters = [0]*26
            for c in word:
                letters[ord(c) - ord('a')] += 1
            key = tuple(letters)
            v[key].append(word)

        return list(v.values())