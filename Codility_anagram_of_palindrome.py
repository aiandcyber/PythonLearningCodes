def solution(s):
    odd = 0

    # Count frequency using two loops
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1
        if count % 2 != 0:
            odd += 1
        if odd > 1:
            return False
    return True

s = "carrace"
print(solution(s))