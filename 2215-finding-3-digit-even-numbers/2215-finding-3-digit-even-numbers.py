class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        s = set()
        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and k != j:
                        temp = str(digits[i]) + str(digits[j]) + str(digits[k])
                        if temp[0] != '0' and int(temp[-1])%2 == 0 and temp not in s:
                            ans.append(int(temp))
                            s.add(temp)
        
        return sorted(ans)