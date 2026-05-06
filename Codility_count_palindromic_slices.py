# problem to count the number of palindromic slices in a string, only the consecutive characters
def solution(A):
    c = 0
    def slice_count(i,j):
        nonlocal c
        while i >=0 and j < len(A) and A[i] == A[j]:
            c += 1
            i -= 1
            j += 1

    for i in range(len(A)):
        slice_count(i,i)
        slice_count(i,i+1)

    return c
A = "abba"
print(solution(A))

