def solution(A):
    B = sorted(A)
    l = len(B)//2
    for i in range(len(B)-1):
        if B[i] != B[i+1]:
            count = 1
        else:
            count += 1
        if count > l:
            d = B[i]
            break
    eq = 0
    c = 0
    d_count = A.count(d)
    for i in range(len(A)):
        if A[i] == d:
            c += 1
        if i+1 < 2*c and len(A)-i-1 < 2*(d_count-c):
            eq += 1
    return eq

A = [4,3,4,4,4,2]
print(solution(A))