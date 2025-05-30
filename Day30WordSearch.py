
class Solution(object):
    def exist(self, board, word):
        def dfs(i, j, k):
            if k == len(word):
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False

            temp = board[i][j]
            board[i][j] = '#'  # mark as visited

            found = (dfs(i+1, j, k+1) or
                     dfs(i-1, j, k+1) or
                     dfs(i, j+1, k+1) or
                     dfs(i, j-1, k+1))

            board[i][j] = temp  # backtrack
            return found

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
