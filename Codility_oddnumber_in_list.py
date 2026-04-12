def solution(list):
    result = 0
    for i in list:
        result ^=i
    return result

list = [1,8,8,8,1,3,2,4,8,2,3]
print(solution(list))