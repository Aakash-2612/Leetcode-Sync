class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        arr = []
        for key, value in d.items():
            arr.append([value, key])
        # print(arr)

        arr.sort()
        ans = []
        index = len(arr)-1
        while k > 0:
            ans.append(arr[index][1])
            k -= 1
            index -= 1
        
        return ans