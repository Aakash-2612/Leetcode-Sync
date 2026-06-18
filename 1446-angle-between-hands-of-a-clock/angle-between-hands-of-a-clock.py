class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        ans = 0
        extra = (minutes/5)*(2.5)
        print(extra)
        t = (minutes/5)
        print(t)
        if t == 0:
            t = 12
        if t < hour:
            # print((hour - t)*30 + extra)
            # print(360 - ((hour - t)*30 + extra))
            ans = min((hour - t)*30 + extra, 360 - ((hour - t)*30 + extra))
        else:
            ans = min((t - hour)*30 - extra, 360 - ((t - hour)*30 - extra))
        return abs(ans)
