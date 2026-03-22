class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        mat2 = []
        mat3 = []
        for i in range(len(mat)-1, -1, -1):
            temp = []
            for j in range(len(mat[0])):
                temp.append(mat[j][i])
            mat2.append(temp)
        # print(mat2)
        for i in range(len(mat)-1, -1, -1):
            temp = []
            for j in range(len(mat[0])):
                temp.append(mat2[j][i])
            mat3.append(temp)
        # print(mat3)
        mat4 = []
        for i in range(len(mat)-1, -1, -1):
            temp = []
            for j in range(len(mat[0])):
                temp.append(mat3[j][i])
            mat4.append(temp)
        # print(mat4)
        if target == mat or target == mat2 or target == mat3 or target == mat4:
            return True
        return False
