class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        min_heap = [i for i in nums]
        heapq.heapify(min_heap)
        while len(min_heap) >= 2:
            cur1 = heapq.heappop(min_heap)
            cur2 = heapq.heappop(min_heap)
            mi = min(cur1, cur2)
            ma = max(cur1, cur2)
            if mi >= k:
                break
            val = mi * 2 + ma
            heapq.heappush(min_heap, val)
            count += 1
        
        return count
        