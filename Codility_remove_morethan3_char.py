def solution(A):
    if len(A) < 3:
        return A
    result = [A[0], A[1]]
    for i in range(2, len(A)):
        if not A[i] == A[i-1] == A[i-2]:
            result.append(A[i])
    # print(result)
    return "".join(result)

# another metod of doing it
def second_solution(A):
    if len(A) < 3:
        return A
    result = A[0:2]
    for i in range(2, len(A)):
        if not A[i] == A[i-1] == A[i-2]:
            result +=A[i]
    # print(result)
    return result

A = "aaaxxbbbbbbbbbbbbbbbbbbcc"
print(solution(A))
print(second_solution(A))