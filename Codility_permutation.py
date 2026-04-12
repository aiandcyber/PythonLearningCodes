def solution(A):
    if not len(A):
        return 0
    if min(A) < 1:
        return 0
    if max(A) > len(A):
        return 0
    A_set = set(A)
    if len(A) != len(A_set):
        return 0
    else:
        return 1

A = [2,1,3,4,5,]
print(solution(A))


