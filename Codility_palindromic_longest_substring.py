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

def solution_2(A):
    ml = 1
    n = len(A)
    d = [[0] * n for _ in range(n)]
    st = 0
    # assign 1 for diagnal elements, char in itself is a palindrome
    for i in range(n):
        d[i][i] = 1
    # check for 2 char length string
    for i in range(n-1):
        if A[i] == A[i+1]:
            d[i][i+1] = 1
            if ml == 1:
                ml = 2
                st = i
    # check for 3 more more char length string
    for l in range(3, n-1):
        for i in range(n - l + 1):
            j = i + l - 1
            if A[i] == A[j] and d[i+1][j-1]:
                d[i][j] = 1
                if l > ml:
                    ml = l
                    st = i
    return A[st:st + ml]

s = "forgeeksskeegfor"
print(solution(s))
print(solution_2(s))
