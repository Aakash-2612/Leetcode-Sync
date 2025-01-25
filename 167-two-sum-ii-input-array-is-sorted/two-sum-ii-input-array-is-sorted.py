class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        ans = []
        index = 1
        for i in numbers:
            if (target - i) in d:
                ans.extend([d[(target - i)], index])
                break
            d[i] = index
            index += 1
        return ans