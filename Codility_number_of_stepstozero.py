def solution(A):
    A = A.lstrip('0')
    if not A:
        return 0
    one = A.count('1')
    zero = A.count('0')
    return 2 * one + zero - 1

A = "011100"
print(solution(A))