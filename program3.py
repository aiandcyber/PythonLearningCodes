""" program 3 start
# program to generate fibnacci series using While loop
n=int(input("input number:"))
a=0
b=1
while a <=n:
    print(a)
    c=a+b
    a=b
    b=c

days=['Monda', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    print(day)

    # program 3 ends """

# program to identify longest binary gap
# while loop to validate input 
while True:
    try:
        n=int(input("input the number between 2 and 1000:"))
        if 2 <= n <= 1000:
            break
        else:
            print("please enter a valid input")
    except ValueError or TypeError:
            print("please enter an intiger value")
print(type(n))
binary=bin(n)[2:]
print(binary)
count=0
max_count=0
for i in binary: 
    print(i)
    if i == "0":
        print("inside")
        count+=1
    else:
        max_count=max(max_count, count)
        count=0
print(f"longest binary gap is: {max_count}")

