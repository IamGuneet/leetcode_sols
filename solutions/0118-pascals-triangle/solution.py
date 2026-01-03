class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        output=[]
        for i in range(numRows):
            row = [1]
            for j in range(1,i):
                val = output[i-1][j-1]+output[i-1][j]
                row.append(val)
            if i>0:
                row.append(1)
            output.append(row)
        return output            

