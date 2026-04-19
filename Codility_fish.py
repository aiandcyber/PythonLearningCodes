def solution(A,B):
    eaten = 0
    stack = []
    for i in range(len(B)):
        if B[i] == 1:
            stack.append(A[i])
        elif B[i] == 0:
            while len(stack):
                if stack[-1] > A[i]:
                    eaten += 1
                    break
                else:
                    stack.pop()
                    eaten += 1
    return_value = len(B) - eaten
    return return_value

A = [4, 3, 2, 1, 5]
B = [0,1,0,0,0]
print(solution(A,B))
