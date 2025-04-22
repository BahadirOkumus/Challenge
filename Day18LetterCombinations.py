class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        result = [""]
        for digit in digits:
            if digit not in mapping:
                continue
            temp = []
            for prefix in result:
                for letter in mapping[digit]:
                    temp.append(prefix + letter)
            result = temp
        return result
