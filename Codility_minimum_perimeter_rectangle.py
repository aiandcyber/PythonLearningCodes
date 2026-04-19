def solution(A):
    for i in range(int(A**0.5), 0, -1):
        if A%i == 0:
            return int(2*(i+(A/i)))

A = 30
print(solution(A))
