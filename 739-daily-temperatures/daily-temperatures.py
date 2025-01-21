class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]* len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                stk_i, stk_temp = stack.pop()
                ans[stk_i] = i - stk_i

            stack.append((i, temperatures[i]))
        
        return ans