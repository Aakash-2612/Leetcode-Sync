class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        drop = set()
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
                drop.add(i-1)
            i += 1
        
        ans = []
        for index, i in enumerate(intervals):
            if index not in drop:
                ans.append(i)
        return ans