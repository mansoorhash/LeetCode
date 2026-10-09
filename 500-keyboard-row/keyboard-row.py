class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = {
            1: "qwertyuiop",
            2: "asdfghjkl",
            3: "zxcvbnm"
        }
        result = []
        for w in words:
            chosenRow = 0
            for c in w.lower():
                if not chosenRow:
                    for r, v in rows.items():
                        if c in v:
                            chosenRow = r
                elif c not in rows[chosenRow]:
                    chosenRow = 0
                    break
            if chosenRow: result.append(w)
        return result

        
