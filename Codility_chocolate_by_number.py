
def gcd(a,b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b,a%b)
    
def solution(N,M):
    g = gcd(N,M)
    return int(N/g)

N = 10
M = 4
print(solution(N,M))
    
