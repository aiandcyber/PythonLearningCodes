def Roate(List, k):
    rotate_length = k % len(List)
    print(rotate_length)
    if not len(List):
        return List
    if rotate_length == 0:
        return List
    head = List[:-rotate_length]
    tail = List[len(List) - rotate_length:]
    print(head)
    print(tail)
    return tail + head

List = [1, 2, 3, 4, 5,6,7,8]
k = 3
print(Roate(List, k))