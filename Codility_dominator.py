def solution(A):
    if len(A) == 0:
        return -1
    if len(A) == 1:
        return 0
    count = 1
    B = sorted(A)
    l = len(B)//2
    for i in range(len(B)-1):
        if B[i] != B[i+1]:
            count = 1
        else:
            count += 1
        if count > l:
            return A.index(B[i])
    return -1

A = [1,4,3,2,3,-1,3,3,3]
print(solution(A))