class Solution:
    def minSwaps(self, s: str) -> int:
        d1 = {'0': 0, '1': 0}
        d2 = {'0': 0, '1': 0}
        temp = 1
        for i in s:
            if int(i) != int(temp):
                d1[i] += 1
            else:
                d2[i] += 1
            temp = not temp

        # print(d1)
        # print(d2)
        if d1['1'] != d1['0'] and d2['0'] != d2['1']:
            return -1
        else:   
            if d1['1'] == d1['0']:
                ans1 = d1['1']
                if d2['1'] == d2['0']:
                    return min(ans1, d2['1'])
                else:
                    return ans1
            else:
                return d2['1']