def solution(A):
    m = A[0]
    s = 0
    for i in range(len(A)):
        s += A[i]
        m = max(m,s)
        if s < 0:
            s = 0
    return m
A = [3,2,-6,4,0]
print(solution(A))
