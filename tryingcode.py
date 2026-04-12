"""
a = 8
b = 5
print(a%b)
"""

list = [1,8,8,8,1,3,2,4,8,2,3]
unduplicate = set(list)
result = 0
for i in list:
    result ^= i
    print(result)
print(unduplicate)
print(list)
print(result)


# integer to binary conversion 
"""
integer = input("enter value:")
binary = bin(int(integer))[2:]
print(f"integer:{integer}, binary:{binary}, converted integer:{int(binary,2)}")
"""