def solution(X,A):
    for index, value in enumerate(A):
        if value >= X:
            return index
    retrun -1

A = [1, 3, 1, 4, 2, 3, 5, 4]
X = 5
print(solution(X,A))
