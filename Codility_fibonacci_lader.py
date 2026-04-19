def solution(A,B):
    l = max(A)
    f = [0]*(l+2)
    result = [0]*len(A)
    f[1] = 1
    for i in range(2, l+2):
        f[i] = f[i-1]+f[i-2]
    for j in range(len(A)):
        result[j] = f[A[j]+1] & (2**B[j]-1)
    return result

A = [4,4,5,5,1]
B = [3,2,4,3,1]
print(solution(A,B))

"""
# Algorithm for fibonacci numbers
def fibo(N):
    if n <=1:
        return n
    f[0] = [0]*(N+2)
    f[1] = 1
    for i in range(2,N+1):
        f[i] = f[i-1] + f[i-2]
    return f
"""