
class Solution(object):
    def restoreIpAddresses(self, s):
        def is_valid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            return 0 <= int(segment) <= 255

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append('.'.join(path))
                return

            for end in range(start + 1, min(start + 4, len(s) + 1)):
                segment = s[start:end]
                if is_valid(segment):
                    backtrack(end, path + [segment])

        res = []
        backtrack(0, [])
        return res

# Example usage
sol = Solution()
print sol.restoreIpAddresses("25525511135")
