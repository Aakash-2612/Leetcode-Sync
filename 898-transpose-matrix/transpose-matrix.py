class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        # print(rows, cols)
        for i in range(cols):
            temp = []
            for j in range(rows):
                temp.append(matrix[j][i])
            ans.append(temp[:])
        
        return ans