def solution(A):
    east = passing = 0
    for i in A:
        if i == 0:
            east += 1
        else:
            passing += east
        if passing > 1000000000:
            return -1
            # break
    return passing

A = [0,1,0,1,1]
print(solution(A))
