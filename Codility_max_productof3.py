def solution(A):
    A.sort()
    last_three = A[-1]*A[-2]*A[-3]
    first = A[0]*A[1]*A[-1]
    # print(A)
    return max(last_three, first)

A = [-10, 20, 5, 0, 1, 3, 4, 5, 6]
print(solution(A))