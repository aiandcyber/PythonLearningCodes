
""" Program 1 start
# Program which take a number input to generate interted pyramid of stars
n = int(input("enter the number:")) # get input
for i in range(n, 0, -1):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2*i-1):
        print('*', end='')  # Print on same line (no newline)
    print() # new line after every row

Program 1 ends """

""" program 2 start 
# program to count the number digit in a input number
n = int(input("enter the number:")) # get input
count = 0
while n > 0:
    n = n // 10
    count+=1
print(f"the number of digits in the input number is {count}")

# same program using for loop
m=input("enter the number:")
for_count=0
for i in m :
    for_count+=1
print(f"the number using ror loop is {count}")

# program 2 ends """


