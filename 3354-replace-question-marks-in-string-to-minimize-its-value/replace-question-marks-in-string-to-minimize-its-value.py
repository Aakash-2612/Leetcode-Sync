class Solution:
    def minimizeStringValue(self, s: str) -> str:
        d = {chr(key): -1 for key in range(97, 123)}
        for i in s:
            if i.isalpha():
                d[i] += 1
        min_heap = [[value, key] for key, value in d.items()]
        heapq.heapify(min_heap)
        # print(min_heap)

        ans = []
        res = ''
        for i in s:
            if i == '?':
                cur = heapq.heappop(min_heap)
                ans.append(cur[1])
                cur[0] += 1
                heapq.heappush(min_heap, cur)
        
        ind = 0
        ans.sort()
        # print(ans)
        for i in s:
            if i == '?':
                res += ans[ind]
                ind += 1
            else:
                res += i
        return res


