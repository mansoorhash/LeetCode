class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []

        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]

            elif newInterval[0] > interval[1]:
                result.append(interval)

            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)
        return result