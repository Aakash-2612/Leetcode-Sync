class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d = {}
        ans = float("inf")
        for ind, i in enumerate(nums):
            if i not in d:
                # print('if')
                d[i] = [(ind, 0)]
            else:
                # print('else')
                if len(d[i]) >= 2:
                    inde, diff = d[i][-1]
                    third_point = ind - (inde - diff)
                    second_value = ind - inde
                    temp = diff + third_point + second_value
                    print(temp)
                    ans = min(ans, temp)
                    d[i].append([ind, (ind - inde)])
                else:
                    prev = d[i][-1]
                    d[i].append([ind, ind-prev[0]])

        # print(d)
        return ans if ans != float('inf') else -1