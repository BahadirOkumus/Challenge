def length_of_longest_substring(s: str) -> int:
    char_dict = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        if s[end] in char_dict:
            start = max(start, char_dict[s[end]] + 1)
        
        char_dict[s[end]] = end
        
        max_length = max(max_length, end - start + 1)
    
    return max_length

