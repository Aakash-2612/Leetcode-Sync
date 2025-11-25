class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        sett = set()
        rem = 1 % k
        s_len = 1
        while rem not in sett:
            if rem == 0:
                return s_len
            sett.add(rem)
            rem = (rem * 10 + 1) % k
            s_len += 1
        return -1