def solution(x, y, d):
    jumps = (y-x)//d
    if (y-x)%d != 0:
        jumps +=1
    return jumps

print(solution(10, 85, 30))
print(solution(10,10,10))
print(solution(1,10,10))
print(solution(5,52,5))