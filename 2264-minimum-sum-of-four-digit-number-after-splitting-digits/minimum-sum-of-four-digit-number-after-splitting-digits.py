class Solution:
    def minimumSum(self, num: int) -> int:
        arr = [i for i in str(num)]
        arr.sort()
        num1 = str(arr[0]) + str(arr[2])
        num2 = str(arr[1]) + str(arr[3])
        return int(num1) + int(num2)