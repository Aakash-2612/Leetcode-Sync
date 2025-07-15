class Solution:
    def isValid(self, word: str) -> bool:
        lenW = False
        digW = False
        voW = False
        conW = False
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if len(word) >= 3:
            lenW = True
        if word.isalnum():
            digW = True
        for i in word:
            if i in vowel:
                voW = True
            else:
                if ord(i) in range(97, 123) or ord(i) in range(65, 91):
                    # print(i)
                    conW = True

        if lenW and digW and voW and conW:
            return True
        else:
            return False