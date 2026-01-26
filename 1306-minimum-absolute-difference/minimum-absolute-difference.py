class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)
        min_diff = float("inf")
        for i in range(len(nums)-1):
            min_diff = min(min_diff, abs(nums[i] - nums[i+1]))
        # print(min_diff)

        s = set()
        min_heap = []
        heapq.heapify(min_heap)
        ans = []
        for i in arr:
            if i - min_diff in s:
                s.add(i)
                first = i-min_diff
                second = i
                heapq.heappush(min_heap, [first, second])
            if  i + min_diff in s:
                s.add(i)
                first = i
                second = i+min_diff
                heapq.heappush(min_heap, [first, second])
            else:
                s.add(i)
        
        while min_heap:
            ans.append(heapq.heappop(min_heap))
        
        return ans