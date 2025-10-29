class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            cur_sum = 0
            for j in range(i, len(arr)):
                cur_sum += arr[j]
                if (j - i + 1) % 2 != 0:
                    # print(arr[i:j+1])
                    ans += cur_sum
        return ans