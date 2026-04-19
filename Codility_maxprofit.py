def solution(A):
    mp = 0
    low = A[0]
    for price in A:
        low = min(low, price)
        mp = max(mp, price-low)
    return mp
A = [23171,21011,21123,21366,21013,21367]
print(solution(A))