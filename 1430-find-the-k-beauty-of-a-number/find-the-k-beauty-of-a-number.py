class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        l = 0
        ans = 0
        num = str(num)
        for r in range(len(num)):
            if (r - l + 1)% k == 0:
                print(int(num[l:r+1]))
                try:
                    if int(num) % int(num[l:r+1]) == 0:
                        ans += 1
                    l += 1
                except:
                    l += 1
    
        return ans