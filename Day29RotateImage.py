class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        
        # Step 1: Transpose the matrix
        for i in xrange(n):
            for j in xrange(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Step 2: Reverse each row
        for i in xrange(n):
            matrix[i].reverse()
