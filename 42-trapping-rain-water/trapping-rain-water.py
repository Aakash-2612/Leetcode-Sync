class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        temp = 0
        l = 0
        arr = []
        for r in range(len(height)):
            if height[l] <= height[r]:
                ans += temp
                arr = []
                temp = 0
                l = r
            else:
                temp += height[l] - height[r]
                arr.append(height[r])
        print(ans)
        print(arr)
        if arr:
            stack = [arr[-1]]
            res = 0
            for i in range(len(arr)-2, -1, -1):
                if stack and arr[i] < stack[-1]:
                    res += stack[-1] - arr[i]
                elif stack and arr[i] > stack[-1]:
                    stack.pop()
                    stack.append(arr[i])
            ans += res
        return ans