def solution(A):
    i = 1
    f = 0
    while i*i < A:
        if A%i == 0:
            f += 2
        i += 1
    if i*i == A:
        f +=1
    return f

A = 24
print(solution(A))
