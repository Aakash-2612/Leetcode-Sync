class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        first = 0
        prev = 0

        for n in derived:
            if n:
                prev = ~prev
        
        return first == prev