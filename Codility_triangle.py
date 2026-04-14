def solution(A):
    def is_triangle(p, q, r):
        if p+q > r and q+r > p and r+p > q:
            return True
        else:
            return False
    A.sort()
    for i in range(len(A) - 2):
        if is_triangle(A[i], A[i+1], A[i+2]):
            return 1
    return 0

A = [10,2,5,1,8,20]
print(solution(A))