# program to find the smallest missing integer
# the array only has positive intigers
def solution(list):
    full_list = range(1, len(list)+2)
    return sum(full_list) - sum(list)

list = [1,2,3,4,5, 6,7,8,9,11]
print(solution(list))
