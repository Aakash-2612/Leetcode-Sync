class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_heap = [[-j, i] for i, j in boxTypes]
        heapq.heapify(max_heap)
        # print(max_heap)

        ans = 0
        while max_heap and truckSize:
            cur = heapq.heappop(max_heap)
            unit, box = -cur[0], cur[1]
            if truckSize < box:
                box -= truckSize
                ans += truckSize * unit
                truckSize = 0
            else:
                truckSize -= box
                ans += box * unit
                box = 0
            
        return ans