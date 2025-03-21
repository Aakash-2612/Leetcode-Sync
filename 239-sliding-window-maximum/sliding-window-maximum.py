class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        max_heap = [[-nums[i], i] for i in range(k)]
        heapq.heapify(max_heap)
        
        ans.append(-max_heap[0][0])
        
        for i in range(k, len(nums)):
            heapq.heappush(max_heap, [-nums[i], i])
            
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            ans.append(-max_heap[0][0])
        
        return ans