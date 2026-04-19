def solution(A):
    count = 0
    h = 0
    stack = []
    for i in range(len(A)):
        if A[i] > h:
            stack.append(A[i])
            count += 1
            h = A[i]
        elif A[i] < h:
            while len(stack) > 0 and A[i] < stack[-1]:
                stack.pop()
            if len(stack) == 0 or A[i] != stack[-1]:
                count += 1
            h = A[i]
    return count

A = [8,8,5,7,9,8,7,4,8]
print(solution(A))

