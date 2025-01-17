class Solution:
    def clearStars(self, s: str) -> str:
        min_heap = [[ord(s[0]) - ord('a'), s[0], 0, 1]]
        heapq.heapify(min_heap)

        stack = [s[0]]
        for i in range(1, len(s)):
            if s[i] == '*':
                stack.append('')
                cur = heapq.heappop(min_heap)
                cur[3] -= 1
                stack[-cur[2]] = ''
                if cur[3] > 0:
                    heapq.heappush(min_heap, cur)
            else:
                stack.append(s[i])
                cur = [ord(s[i]) - ord('a'), s[i], -i, 1]
                heapq.heappush(min_heap, cur)

        # print(min_heap)
        return ''.join(stack)