class Solution:
    def countStableSubarrays(self, capacity: List[int]) -> int:
        m = Counter() # maps (number, incl sum) -> count
        res = curr = 0
        for r, v in enumerate(capacity):
            curr += v
            res += m[(v, curr - 2 * v)]
            m[(v, curr)] += 1
            res -= r and v == 0 and capacity[r-1] == 0 # dedupe [0, 0] pairs
        return res