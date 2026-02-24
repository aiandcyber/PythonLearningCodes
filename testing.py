"""
my_list=[-1,3,2,2,3,4,5,]
print(f"my list is{my_list}")
# my_list.sort()
# print(f"sorted list is: {my_list}")
my_set=set(my_list)
print(f"my set is{my_set}")
my_new_set = sorted(my_set)
print(f"sorted set is: {my_new_set}")
"""
"""
my_dict = {"[":"]", "{":"}", "(":")"}
print(f"original dict: {my_dict}")
stack = ["[", "]"]
popped = stack.pop()
print(f"popped: {popped} and new stack: {stack}")
"""
import math

integer = 30
root=int(math.sqrt(integer))
power=int(integer**0.5)
print(f"{root}")
print(f"{power}")
