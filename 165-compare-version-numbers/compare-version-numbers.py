class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1 = version1.split('.')
        arr2 = version2.split('.')

        diff = abs(len(arr1) - len(arr2))
        if len(arr1) < len(arr2):
            arr1 += [0]*diff
        else:
            arr2 += [0]*diff
        for i, j in zip(arr1, arr2):
            if int(i) < int(j):
                return -1
            elif int(i) > int(j):
                return 1
            
        return 0