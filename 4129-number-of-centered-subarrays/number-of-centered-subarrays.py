class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            s = set()
            tot = 0
            s.add(nums[i])
            for j in range(i, len(nums)):
                # print(nums[i:j+1])
                s.add(nums[j])
                tot += nums[j]
                if tot in s:
                    # print(f'{tot=}')
                    count += 1
        
        return count