class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for index, i in enumerate(s):
            d[i] = index

        res = []
        size, end = 0, 0
        for index, i in enumerate(s):
            size += 1
            end = max(end, d[i])

            if index == end:
                res.append(size)
                size = 0

        return res