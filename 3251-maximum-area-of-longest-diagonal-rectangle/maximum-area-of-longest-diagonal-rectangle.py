class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        cur_max = 0
        max_area = 0
        for i in dimensions:
            l = i[0]
            w = i[1]
            diag = (l * l + w * w)**0.5
            area = l * w
            if diag == cur_max:
                cur_max = diag
                max_area = max(area, max_area)
            elif diag > cur_max:
                cur_max = diag
                max_area = area
        
        return max_area