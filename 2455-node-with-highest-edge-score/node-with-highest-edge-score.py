class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        from collections import defaultdict

        h = defaultdict(int)
        w = 0
        for score, node in enumerate(edges):
            h[node] += score
            if h[node] > h[w] or (h[w] == h[node] and node < w):
                w = node
        return w