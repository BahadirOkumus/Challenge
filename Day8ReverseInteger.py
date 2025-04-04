def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    res = 0
    neg = x < 0
    x = abs(x)
    
    while x:
        digit = x % 10
        x //= 10
        
        if res > (INT_MAX - digit) // 10:
            return 0
        
        res = res * 10 + digit

    return -res if neg else res
