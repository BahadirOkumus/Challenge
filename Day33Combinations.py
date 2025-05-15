class Solution(object):
    def combine(self, n, k):
        res = []
        def backtrack(start, path):
            if len(path) == k:
                res.append(list(path))
                return
            for i in xrange(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()
        backtrack(1, [])
        return res
