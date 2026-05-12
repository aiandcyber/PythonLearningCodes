def solution(A, K, L):
    for i in A:
        if max(A) > K or A.count(i) > L :
            return False
    return True if len(A) > 0 else False
# count[i] = A.get(i,0) - the get function also return the number of count of value i in A. If no value, then return 0
A = [1, 2, 3, 4, 5]
K = 6
L = 1
print(solution(A, K, L))