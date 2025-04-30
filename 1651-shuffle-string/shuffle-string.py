class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        arr = ['0'] * len(s)
        for i, j in zip(s, indices):
            arr[j] = i
        return ''.join(arr)