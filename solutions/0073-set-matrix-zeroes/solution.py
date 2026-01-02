class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """
        r_len = len(matrix)
        c_len = len(matrix[0])
        row = [0]*r_len
        col = [0]*c_len
        for i in range(r_len):
            for j in range(c_len):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
            
        for i in range(r_len):
            for j in range(c_len):
                if row[i] == 1 or col[j] == 1:
                    matrix[i][j]=0

                
