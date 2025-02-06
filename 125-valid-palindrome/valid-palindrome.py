class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if i.isalnum():
                arr.append(i.lower())
        
        return arr[::-1] == arr