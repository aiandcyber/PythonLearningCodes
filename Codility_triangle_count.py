def solution(A):
    A.sort()
    count = 0
    print(A)
    for i in range(len(A) - 2):
        k = i+2
        for j in range(i+1, len(A)-1):
            while k < len(A) and A[i]+A[j] > A[k]:
                k += 1
            count += k-j-1
    return count

A = [10,2,5,1,8,12]
print(solution(A))