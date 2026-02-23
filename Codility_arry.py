# program to reverese an array
my_list=[1,2,3,4,5,6,7,8,9]
start=0
end=len(my_list)-1
while start < end:
    my_list[start], my_list[end]=my_list[end], my_list[start]
    start+=1
    end-=1
print(my_list)

# program to calculate sum of consecutive numbers
n=int(input("input the number:"))
result=0
for i in range(n):
    result+=(i+1)
    print(result)
print(f"result is: {result}")

# program to calculate sum on consecutive numbers using function

def addition(num):
    sum=num*(num+1)//2
    return sum

sum=addition(n)
print(f"sum using function: {sum}")