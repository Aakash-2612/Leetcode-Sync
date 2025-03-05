class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        ans = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                ans.append([arr[i]/arr[j], arr[i], arr[j]])
        
        # print(ans)
        heapq.heapify(ans)
        cur = 0
        while k:
            cur = heapq.heappop(ans)
            k -= 1
        
        return [cur[1], cur[2]]
