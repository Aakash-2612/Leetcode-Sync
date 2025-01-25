class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        ans = []
        while l < r:
            tot = numbers[l] + numbers[r]
            if tot == target:
                ans.extend([l+1, r+1])
                break
            elif tot > target:
                r -= 1
            else:
                l += 1
        
        return ans