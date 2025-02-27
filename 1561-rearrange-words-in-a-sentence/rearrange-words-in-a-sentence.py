class Solution:
    def arrangeWords(self, text: str) -> str:
        min_heap = [[len(i), index, i.lower()] for index, i in enumerate(text.split())]
        # print(min_heap)
        heapq.heapify(min_heap)
        ans = []
        while min_heap:
            cur = heapq.heappop(min_heap)
            ans.append(cur[2])
        
        res = ' '.join(ans)
        res = res[0].upper() + res[1:]
        return res