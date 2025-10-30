class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        arr = [i-1 for i in target]
        print(arr)
        cur_sum = 0
        ans = 1
        for i in arr:
            if i == 0:
                cur_sum = 0
            else:
                if cur_sum < i:
                    ans += (i - cur_sum)
                    cur_sum += (i - cur_sum)
                else:
                    cur_sum = i
        
        return ans