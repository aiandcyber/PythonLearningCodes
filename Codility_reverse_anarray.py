# program to reverese an array
def solution(my_list):
    start=0
    end=len(my_list)-1
    while start < end:
        my_list[start], my_list[end]=my_list[end], my_list[start]
        start+=1
        end-=1
    return my_list
    
A=[1,2,3,4,5,6,7,8,9]
print(solution(A))