class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        from collections import deque
        res = []
        q = deque(mapping[digits[0]])
        for n in digits[1:]:
            n_list = []
            if n in mapping:
                while q:
                    val = q.popleft()
                    for c in mapping[n]:
                        n_list.append(val+c)
                q = deque(n_list)

        return list(q)

