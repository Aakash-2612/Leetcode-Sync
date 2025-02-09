class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {} # Empty dictionary
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # print(d)
        # After this loop we will have the counts of the elements in our d
        
        arr = [] # temperaory array to store the key and values
        for key, value in d.items():
            arr.append([value, key])
        # print(arr)

        arr.sort() # sorting the array in ascending order
        ans = [] # final array which will store my final answer
        index = len(arr)-1 # index variable that will help me access the elements
        while k > 0:
            ans.append(arr[index][1]) # i just want the element so i am taking the index [1]
            k -= 1 # this will decrement the k value till it reaches 0
            index -= 1
        
        return ans # returning my final answer array