def solution(N):
    binary = bin(N)[2:]
    max_count = 0
    count = 0
    for i in binary:
        if i == "0":
            count +=1
        else:
            max_count = max(count, max_count)
            count = 0
    return max_count

integer = input("enter the integer:")
N=int(integer)
print(solution(N))

