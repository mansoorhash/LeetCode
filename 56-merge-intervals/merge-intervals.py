class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        result = [intervals[0]]
        for inter in intervals[1:]:
            if inter[0] <= result[-1][1]:
                if result[-1][1] < inter[1]:
                    result[-1][1] = inter[1]
            else:
                result.append(inter)

        return result
                

        