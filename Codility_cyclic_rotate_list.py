def Roate(List, k):
    if not List:
        return List
    rotate_length = k % len(List)
    head = List[:-rotate_length]
    tail = List[len(List) - rotate_length:]
    return tail + head

List = [1, 2, 3, 4, 5,6,7,8]
k = 3
print(Roate(List, k))