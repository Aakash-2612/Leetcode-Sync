class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        start = int(area**(0.5))

        for i in range(start, area+1):
            if (area%i) == 0 and (i >= (area//i)):
                return [i, area//i]
        