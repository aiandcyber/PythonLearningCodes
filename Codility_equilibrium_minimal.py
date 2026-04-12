def solution(list):
    # best = None
    left_sum = 0
    right_sum = sum(list)
    best = right_sum
    for i in range(0, len(list)-1):
        left_sum += list[i]
        right_sum -= list[i]
        difference = abs(left_sum - right_sum)
        print(difference)
        # if best is None:
        #    best = difference
        if difference < best:
            best = difference
    return best

list = [1, 3, 6, 5, 6, 100]
print(solution(list))