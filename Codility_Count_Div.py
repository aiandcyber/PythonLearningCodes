# program to find the number of dvisible numbers by K between A, B
def solution(A,B,K):
    m1 = B//K
    m2 = (A-1)//K
    return m1-m2

A = 6
B = 11
K = 2
print(solution(A,B,K))