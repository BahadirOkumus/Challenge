class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        result_str = ''.join(str(d) for d in result).lstrip('0')
        return result_str or "0"

# Example usage
if __name__ == "__main__":
    s = Solution()
    print s.multiply("123", "456")  # Output: "56088"
