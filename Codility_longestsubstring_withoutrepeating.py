def solution(A):
    seen = {}
    l = 0
    length = 0
    for r in range(len(A)):
        char = A[r]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            length = max(length, r-l+1)
        seen[char] = r
    return length

A = "abcacbdd"
print(solution(A))