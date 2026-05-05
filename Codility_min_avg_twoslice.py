# solution to find the minimum average of slice of at least 2 elements
def solution(A):
    la = 10000
    li = 0
    p2 = 10000
    p1 = 10000
    for idx, i in enumerate(A):
        a3 = (p2+p1+i)/3.0
        if a3 < la:
            la = a3
            li = idx-2
        a2 = (p1+i)/2.0
        if a2 < la:
            la = a2
            li = idx-1
        p2 = p1
        p1 = i
    return li

A = [4, 2, 2, 5, 1, 5, 8]
print(solution(A))
