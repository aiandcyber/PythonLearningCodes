# problems related to palindrome
def solution(S):
    S = S.lower() # convert to lowercase
    S = S.replace(" ", "") # remove spaces
    return S == S[::-1] # check if the string is the same as the reverse of the string

S = "abba"
print(solution(S))

