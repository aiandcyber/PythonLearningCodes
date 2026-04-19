def solution(S):
    brackets = {"{":"}", "(":")", "[":"]"}
    result = []
    if len(S) == 0:
        return 1
    for i in S:
        if i in brackets.keys():
            result.append(brackets[i])
        elif i in brackets.values():
            if len(result) == 0:
                return 0
            if result[-1] == i:
                result.pop()
    if len(result) == 0:
        return 1
    else:
        return 0

S = ["{","[","(",")","(",")","]","}"]
print(solution(S))