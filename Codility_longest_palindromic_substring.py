def solution(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # dp[i][j] if the substring from [i to j] is a palindrome or not
    start = 0
    maxLen = 1
    
    # all substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = 1
    
    # check for substrings of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = 1
            if maxLen < 2:
                start = i
                maxLen = 2
    
    # check for substrings of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
    
            # if s[i] == s[j] then check for [i+1 .. j-1]
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = 1
                if length > maxLen:
                    start = i
                    maxLen = length
    
    return s[start:start + maxLen]

s = "forgeeksskeegfor"
print(solution(s))
