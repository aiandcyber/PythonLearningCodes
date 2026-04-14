def solution(A):
    brackets = {"{":"}", "(":")", "[":"]"}
    result = []
    if len(A) ==0:
        return 1
    for i in A:
        if i in brackets.keys():
            append_value = brackets.???
            result.append(append_value)
        elif i in brackets.values():
            if len(result) == 0:
                return 0
            if result[-1] == i:
                result.pop()
    if len(result) == 0:
        return 1
    else:
        return 0

A = ["{","[","(",")","(",")","]","}"]
print(solution(A))