list = [1, 2, 4, 46, 6, 11]
def search(list):
    if len(list) == 1:
        return list[0]
    max = search(list[1:])
    return list[0] if list[0] > max else max
max = search(list)
print(max)