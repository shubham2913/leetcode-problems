class Solution:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        matrix1=[[0]*n for i in range(n)]
        for i in range(n) :
            for j in range(n) :
                matrix1[i][j]=matrix[i][j]
        #print(matrix1)
        for i in range(n) :
            for j in range(n) :
                #print(n-1-i,j,matrix1[n-1-i][j])
                matrix[j][i]=matrix1[n-1-i][j]
        #print(matrix1)