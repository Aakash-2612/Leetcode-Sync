class Solution:
    def findScore(self, nums: List[int]) -> int:
        d = {}
        min_heap = [(i, index) for index, i in enumerate(nums)]
        heapq.heapify(min_heap)

        s = 0
        while len(d) < len(nums):
            cur = heapq.heappop(min_heap)
            ind = cur[1]
            if ind not in d:
                d[ind] = 1
                if ind > 0:
                    d[ind - 1] = 1
                if ind < len(nums)-1:
                    d[ind + 1] = 1
                s += cur[0]
        return s