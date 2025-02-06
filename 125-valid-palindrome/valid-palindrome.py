class Solution:
    def isPalindrome(self, s: str) -> bool:
        myStr = ''.join(re.findall(r'[a-zA-Z0-9]+', s)).lower()
        return myStr[::-1] == myStr