# program to finid the smallest missing positive intiger.
# the given array may contain both positive and negative intigers. 
def solution(A):
    A.sort()
    m = 1
    for i in A:
        if i == m:
            m += 1
        if i > m:
            break
    return m

A = [1, 3, 6, 4, 1, 2]
# A = [-1,-3]
print(solution(A))
