def solution(A):
    for i in range(len(A)):
        if A[i] > 0:
            break
        else:
            A[i] = abs(A[i])
    B = set(A)
    return len(B)

A = [-5, -3, -1, 0, 3, 6]
print(solution(A))
