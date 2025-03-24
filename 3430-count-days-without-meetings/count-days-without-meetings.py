class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key= lambda x : x[0])
        # print(meetings)
        
        res = 0
        for i in range(1, len(meetings)):
            if meetings[res][1] >= meetings[i][0]:
                meetings[res][1] = max(meetings[res][1], meetings[i][1])
            else:
                res += 1
                meetings[res] = meetings[i]
        
        arr = meetings[:res+1]
        count = 0
        day = 0
        # print(arr)
        for i in range(len(arr)):
            low = arr[i][0]
            high = arr[i][1]
            
            # print(low, high)
            if day < low:
                count += (low-day)-1
                day = low
                # print(count)
            
            if day == days:
                break
            
            day = high 
            
        if day < days:
            count += (days-day)
            
        return count