# Find the maximum non overlapping segments. This code got 100% in codility test
def solution(A,B):
    # l = min(A) - 1 # This code got 90% score because this command failed for empty list. 
    # l = float('-inf') # assign a lowest number. 
    if len(A) == 0:
        return 0
    # l = A[0]-2
    c = 1
    l = B[0] # start c at 1 and l at B[0] is a better solution than assign a negative lowest number
    for i in range(len(A)):
        if A[i] > l:
            c += 1
            l = B[i]
    return c

A = [1,3,7,9,9]
B = [5,6,8,9,10]
print(solution(A,B))