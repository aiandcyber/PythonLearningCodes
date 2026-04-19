def solution(A,K):
    c = 0
    l = 0
    if K < 1:
        return 0
    if len(A) == 0:
        return 0
    for i in A:
        l += i
        if l >= K:
            c += 1
            l = 0
    return c

A = [1,2,3,4,1,1,3]
K = 4
print(solution(A,K))