class Solution:
    def arrangeWords(self, text: str) -> str:
        min_heap = [[len(i), index, i.lower()] for index, i in enumerate(text.split())]
        # print(min_heap)
        heapq.heapify(min_heap)
        ans = ''
        while min_heap:
            cur = heapq.heappop(min_heap)
            ans += cur[2] + ' '
        
        ans = ans.rstrip()
        return ans[0].upper() + ans[1:]