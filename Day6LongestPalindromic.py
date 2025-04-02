def longest_palindromic_substring(s):
    if not s:
        return ""
    
    start, max_length = 0, 1
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1
    
    for i in range(len(s)):
        l1, len1 = expand_around_center(i, i)  # Odd-length palindrome
        l2, len2 = expand_around_center(i, i + 1)  # Even-length palindrome
        
        if len1 > max_length:
            start, max_length = l1, len1
        if len2 > max_length:
            start, max_length = l2, len2
    
    return s[start:start + max_length]

# Example usage
test_cases = [
    "babad",
    "cbbd",
    "racecar",
    "a",
    "ac",
    "forgeeksskeegfor"
]

for s in test_cases:
    print(f"Input: {s} => Longest Palindromic Substring: {longest_palindromic_substring(s)}")
